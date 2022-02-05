from random import uniform
from salesman import Salesman


class Environment:
  def __init__(self, mutation_prob, pop_size, target_fitness, city_map, max_gens=False):
    self.population = [Salesman(city_map) for _ in range(pop_size)]
    self.mutation_probability = mutation_prob
    self.best = self.population[0]
    self.finished = False
    self.generation = 0
    self.target_fitness = target_fitness
    self.max_gens = max_gens
    self.best_salesmen = []

  def calc_pop_fitness(self):
    for salesman in self.population:
      salesman.calc_fitness()

  def update_best(self):
    for salesman in self.population:
      if salesman.fitness > self.best.fitness:  # New best salesman.
        self.best = salesman
        self.best_salesmen.append(salesman)
      if salesman.fitness >= self.target_fitness:  # Terminate if target fitness already achieved.
        self.finished = True

  def roulette_sample(self):

    #  Get probability intervals:
    total_weight = sum(salesman.fitness for salesman in self.population)
    rel_weight = [salesman.fitness / total_weight for salesman in self.population]
    for i in range(1, len(rel_weight)):
      rel_weight[i] = rel_weight[i] + rel_weight[i - 1]

    #  Binary search the interval random num fits in:
    random_num = uniform(0, rel_weight[-1])
    left, right = 0, len(rel_weight)
    while left < right:
      mid = (left + right) // 2
      if random_num > rel_weight[mid]:
        left = mid + 1
      else:
        right = mid
    return self.population[left]

  def reproduce(self):
    next_generation = []
    for _ in range(len(self.population)):
      parent_a = self.roulette_sample()
      parent_b = self.roulette_sample()
      child = parent_a.crossover(parent_b)
      child.attempt_mutation(self.mutation_probability)
      next_generation.append(child)  # Can't add child to pop we're sampling from.
    self.population = next_generation.copy()

  def display(self):
    print(f"[Gen {self.generation}] Best: '{self.best.path}' Score: {self.best.fitness}")

  def sim(self):
    while not self.finished:
      self.update_best()
      self.reproduce()
      self.calc_pop_fitness()
      self.display()
      self.generation += 1
      if self.max_gens and self.generation > self.max_gens:
        self.finished = True
