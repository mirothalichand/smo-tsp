# smo-tsp
SPIDER MONEKY OPTIMIZATION ALGORITHM FOR TSP

The Spider Monkey Optimization (SMO) algorithm is a metaheuristic algorithm that is inspired by the movement behavior of spider monkeys in nature. The idea behind the SMO algorithm is to use the movement behavior of the monkeys to explore the search space and find good solutions for the TSP problem.

In the TSP problem, each monkey represents a possible solution (a route that visits all the cities) and the fitness of each monkey is evaluated based on the total distance of the route. The SMO algorithm starts with a population of randomly generated monkeys, and in each iteration, it updates the position of the monkeys based on the following rules:

The movement behavior of the monkeys: Each monkey can move to a new position by swapping the positions of two randomly chosen cities in its route. This operation increases the diversity of the population and allows the monkeys to explore new areas of the search space.

The rotation behavior of the monkeys: Each monkey can rotate its route by moving a randomly chosen city to the front of the route. This operation increases the diversity of the population and allows the monkeys to explore new areas of the search space.

The selection behavior of the monkeys: Each monkey is compared to its best neighbor monkey (the monkey with the lowest fitness) and if the current monkey has a higher fitness it will be replaced by its best neighbor.

The algorithm continues until a stopping criterion is met, such as reaching a maximum number of iterations or reaching a satisfactory solution. The best solution found so far is the monkey with the lowest fitness (shortest distance).

The movement behavior of the monkeys allows the algorithm to explore new areas of the search space, while the rotation behavior of the monkeys allows the algorithm to explore different routes of the monkeys. The selection behavior of the monkeys allows the algorithm to keep the best solutions and improve them. The combination of these behaviors makes the SMO algorithm a powerful metaheuristic algorithm for solving the TSP problem.
