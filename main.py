from city_map import CityMap
from environment import Environment
from plotting import plot_cities, plot_fitness


def main():

  # Setup:
  evo_setup = {
    "city_map": CityMap(8, (10, 10)),
    "pop_size": 250,
    "mutation_prob": 0.2,
    "target_fitness": 1,
    "max_gens": 100
  }

  # Simulate evolution:
  environment = Environment(evo_setup)
  environment.sim()
  best_path_sim = environment.best.path
  best_path_sim_dist = evo_setup["city_map"].get_path_dist(best_path_sim)

  # Brute force:
  best_path_bf = evo_setup["city_map"].gen_brute_force()
  best_path_bf_dist = evo_setup["city_map"].get_path_dist(best_path_bf)

  # Visualise:
  plot_cities(evo_setup["city_map"])
  plot_fitness(environment.best_salesmen)
  print(f"[Brute Force] Path: {best_path_bf} with length: {best_path_bf_dist}")
  print(f"[Genetic Algorithm] Path: {best_path_sim} with length: {best_path_sim_dist}")

if __name__ == "main":
  main()
