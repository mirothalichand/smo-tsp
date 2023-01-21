import random
import numpy as np

def TSP_SMO(distance_matrix, num_monkeys, max_iterations, a, b):
    num_cities = len(distance_matrix)
    # Initialize the position of the monkeys (randomly)
    monkeys = [random.sample(range(num_cities), num_cities) for _ in range(num_monkeys)]
    fitness = np.array([evaluate_fitness(monkey, distance_matrix) for monkey in monkeys])
    best_monkey = np.argmin(fitness)
    best_route = monkeys[best_monkey]
    best_distance = fitness[best_monkey]
    for iteration in range(max_iterations):
        for i in range(num_monkeys):
            j = np.random.randint(num_monkeys)
            k = np.random.randint(num_monkeys)
            while k == j:
                k = np.random.randint(num_monkeys)
            new_monkey = mutate_monkey(monkeys[i], monkeys[j], monkeys[k], a, b)
            new_distance = evaluate_fitness(new_monkey, distance_matrix)
            if new_distance < fitness[i]:
                monkeys[i] = new_monkey
                fitness[i] = new_distance
            if new_distance < best_distance:
                best_monkey = i
                best_route = new_monkey
                best_distance = new_distance
    return best_route, best_distance


def evaluate_fitness(route, distance_matrix):
    distance = 0
    for i in range(len(route)-1):
        distance += distance_matrix[route[i]][route[i+1]]
    distance += distance_matrix[route[-1]][route[0]]
    return distance

def mutate_monkey(monkey, monkey1, monkey2, a, b):
    new_monkey = monkey.copy()
    for i in range(len(monkey)):
        if random.uniform(0, 1) < a:
            j = random.randint(0, len(monkey) - 1)
            new_monkey[i], new_monkey[j] = new_monkey[j], new_monkey[i]
        if random.uniform(0, 1) < b:
            new_monkey = np.roll(new_monkey, 1)
    return new_monkey


# Define the distance matrix
distance_matrix = [[0, 10, 20, 30], [10, 0, 15, 25], [20, 15, 0, 20], [30, 25, 20, 0]]

# Define the number of monkeys
num_monkeys = 20

# Define the number of iterations
max_iterations = 1000

# Define the parameter a 
a = 0.2

# Define the parameter b
b = 0.1

# Solve the TSP using the SMO algorithm
best_route, best_distance = TSP_SMO(distance_matrix, num_monkeys, max_iterations, a, b)

# Print the best route and best distance
print("Best route:", best_route)
print("Best distance:", best_distance)

