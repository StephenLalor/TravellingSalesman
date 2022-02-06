import matplotlib.pyplot as plt


def plot_cities(city_map):
  cities_x = [city.x for city in city_map.cities]
  cities_y = [city.y for city in city_map.cities]
  colours = ["yellow"] * len(cities_x)
  colours[0] = "green"
  colours[-1] = "red"
  _, ax = plt.subplots()
  ax.grid(zorder=0)
  ax.scatter(cities_x, cities_y, s=350, zorder=3, color=colours)
  for i in range(1, len(cities_x)):
    from_loc = (cities_x[i], cities_y[i])
    to_loc = (cities_x[i-1], cities_y[i-1])
    plt.annotate(text=f"{i}", xy=from_loc, xytext=to_loc, arrowprops=dict(arrowstyle="->"))
  plt.annotate(text=f"{len(cities_x)}", xy=(cities_x[-1], cities_y[-1]))
  plt.show()

def plot_fitness(best_salesmen):
  generation = range(len(best_salesmen))
  fitness = [salesman.fitness for salesman in best_salesmen]
  _, ax = plt.subplots()
  ax.plot(generation, fitness)
  ax.set(xlabel="Generation", ylabel="Fitness", title="Salesman Fitness")
  ax.grid()
  plt.show()
