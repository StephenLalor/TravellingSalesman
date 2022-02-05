from random import randint, random
from permutations import heaps_algo


class City:
  def __init__(self, name, pop, pos):
    self.name = name
    self.pop = pop
    self.x = pos[0]
    self.y = pos[1]

  def __str__(self):
    return f"Name: {self.name}, Pos: ({self.x}, {self.y}), Pop: {self.pop}"


class CityMap:
  def __init__(self, num_cities, grid_size):
    self.grid_size = grid_size
    self.cities = self.gen_cities(num_cities, grid_size)
    self.dist_cache = self.cache_distance()  # Pre-computed distances.

  def gen_cities(self, num_cities, grid_size):
    chosen = set()  # Positions that are already taken.
    cities = []
    num = 0
    while len(cities) < num_cities:  # Won't be too many cities so this is fine.
      pos = (randint(0, grid_size[0]-1), randint(0, grid_size[1]-1))
      if pos not in chosen:  # Consider time complexity when calling "in".
        chosen.add(pos)
        cities.append(City(num, random(), pos))
        num += 1
    return cities

  def get_cities_coordinates(self):
    return [[city.x, city.y] for city in self.cities]

  def calc_dist(self, city_a_ind, city_b_ind):
    x_diff = self.cities[city_a_ind].x - self.cities[city_b_ind].x
    y_diff = self.cities[city_a_ind].y - self.cities[city_b_ind].y
    return abs(x_diff) + abs(y_diff)  # Relative dist is all that matters.

  def cache_distance(self):
    cache = {}
    for i in range(len(self.cities)):
      for j in range(i+1, len(self.cities)):  # Don't want (1,2) and (2,1) or (2,2) so start at i+1.
        cache[(i, j)] = self.calc_dist(i, j)
    return cache

  def get_cached_dist(self, i, j):
    if (i, j) in self.dist_cache:
      return self.dist_cache[(i, j)]
    if (j, i) in self.dist_cache:  # Also search for reversed. Saves having to actually store it!
      return self.dist_cache[(j, i)]
    raise IndexError(f"Neither {(i, j)} not {(j, i)} in dist_cache!")

  def get_path_dist(self, path):
    tot_dist = 0
    for i in range(1, len(path)):
      tot_dist += self.get_cached_dist(path[i - 1], path[i])
    return tot_dist

  def gen_brute_force(self):
    best_dist = float("Inf")
    best_path = []
    cities_seq = list(range(len(self.cities)))
    perms_generator = heaps_algo(cities_seq, len(self.cities))  # Generate all possible paths.
    for path_perm in perms_generator:
      tot_dist = self.get_path_dist(path_perm)
      if tot_dist < best_dist:  # Update new best path and distance.
        best_dist = tot_dist
        best_path = path_perm.copy()
    return best_path

  def __str__(self):
    lst = [[" . "] * self.grid_size[1] for _ in range(self.grid_size[0])]
    for city in self.cities:
      lst[city.x][city.y] = " " + str(city.name) + " "
    output = []
    for line in lst:
      output += line + ["\n"]
    return "".join(output)
