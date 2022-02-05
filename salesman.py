from random import random, randint
from numpy.random import choice


class Salesman:
  def __init__(self, city_map):
    # TODO: make starting city always the same.
    self.path = choice(len(city_map.cities), len(city_map.cities), replace=False).tolist()
    self.fitness_lower_bound = 0.000005  # Everything has a fitness of at least this minimum level.
    self.fitness = self.fitness_lower_bound
    self.city_map = city_map

  def calc_fitness(self):  # TODO: should incorporate the city pop here somehow.
    tot_dist = self.city_map.get_path_dist(self.path)
    fitness = 1 / (tot_dist + 1)  # Shorter distance is better, so invert.
    self.fitness = max(self.fitness_lower_bound, fitness)

  def crossover(self, other_parent):
    path_len = len(self.path)
    if len(self.path) != len(other_parent.path):
      msg = f"Child must have genes of same length as Parent! ({len(other_parent.path)} Vs {path_len})"
      raise ValueError(msg)
    start = randint(0, path_len)
    end = randint(min(start+1, path_len), path_len)  # Maintain the order of parent's path.
    new_path = self.path[start:end+1]  # Initially take chunk of first parent.
    new_path_members = set(new_path)  # Loop is O(n) so O(1) membership check makes sense.
    for item in other_parent.path:  # Build remaining path.
      if item not in new_path_members:  # O(1) membership check in set.
        new_path_members.add(item)  # A bit messy appending to two things but O(1) each, so worth it.
        new_path.append(item)
        if len(new_path) >= path_len:
          break
    child = Salesman(self.city_map)
    child.path = new_path
    return child

  def attempt_mutation(self, mutation_probability):
    if 0 > mutation_probability > 1:
      raise ValueError("The mutation_probability must be between 0 and 1!")
    for i in range(len(self.path)):  # TODO: Could swap two *neighbours* instead.
      if mutation_probability > random():
        rand_pos = randint(0, len(self.path)-1)  # Random index to swap with.
        self.path[i], self.path[rand_pos] = self.path[rand_pos], self.path[i]

  def __str__(self):
      return f"Path: {self.path}, Fitness: {self.fitness}"
