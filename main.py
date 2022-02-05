from city_map import CityMap
from environment import Environment

def main():
  target_fitness = 1
  initial_pop = 250
  mutation_probability = 0.2
  max_gens = 100

  num_cities = 8
  grid_size = (10, 10)

  city_map = CityMap(num_cities, grid_size)
  best_path = city_map.gen_brute_force() ## SLOW!
  environment = Environment(mutation_probability, initial_pop, target_fitness, city_map, max_gens)
  environment.sim()
  best_sim_path = environment.best.path

  print(city_map)
  print(f"[Brute Force] Path: {best_path} with length: {city_map.get_path_dist(best_path)}")
  print(f"[Genetic Algorithm] Path: {best_sim_path} with length: {city_map.get_path_dist(best_sim_path)}")

if __name__ == "main":
  main()

for salesman in environment.best_salesmen:
  print(salesman)




# TODO: Record the best paths in a list and make a graph.
# TODO: Do documentation on objects.