"""
Easy mizanamet

"""
import random 

def initial_population(population_size, chromosome_length):
    population = []
    for i in range(population_size):
        chromosome = [random.randint(0, 1) for _ in range(chromose_length)]
        population.append(chromosome)
        
    return population

def evaluation_fitness(population):
    fitness_values = []
    for chromosome in population:
        fitness = sum(chromosome)
        fitness_values.append(fitness)
    return fitness_values

def selection(population, fitness_values, num_parents):
    parents = []
    for _ in range(num_parents):
        max_fitness_index = fitness_values.index(max(fitness_values))
        parents.append(population[max_fitness_index])
        fitness_values[max_fitness_index] = -1 # Mark Chromosome as seen
    return parents

def crossover(parents, num_offspring):
    offspring = []
    while len(offspring) < num_offspring:
        parent1 = random.choice(parents)
        parent2 = random.choice(parents)
        cross_over_point = random.randint(1, len(parents) -1) 
        child = parent1[:cross_over_point] + parent2[cross_over_point:]
        offspring.append(child)
    return offspring

def mutation(offspring, mutation_rate):
    for i in range(len(offspring)):
        for j in range(len(offspring[i])):
            if random.random() < mutation_rate:
                offspring[i][j] = 1 - offspring[i][j]
    return offspring


"""
Population size: for using initial population function, to generate POPULATION
Chromosome_length: for initail population Func
num_generation: User Input, For Using in for loop
num_parents: Number of Parents, for using in selection & crossover function
num_offspring: offspring is an array of childs, this argument is Number of Childs
mutation_rate: This algorithm is implemented based on the
 "theory of survival of the fittest".
 We use this argument to select the worthy children
"""


def genetice_algorithms(population_size, chromosome_length, num_generations, 
                      num_parents, num_offspring, mutation_rate):
    population = initial_population(population_size, chromosome_length)
    for generation in range(num_generations):
        fitness_values = evaluation_fitness(population)
        parents = selection(population, fitness_values, num_parents)
        offspring = crossover(parents, num_offspring)
        offspring = mutation(offspring, mutation_rate)
        population = parents + offspring
    best = population[fitness_values.index(max(fitness_values))]
    return best


# Example of usage: 
population_size = 1000
chromose_length = 5
num_generations = 100
num_parents = 40
num_offspring = 20
mutation_rate = 0.45


best = genetice_algorithms(population_size, chromose_length, num_generations,
                           num_parents, num_offspring, mutation_rate)

print(f'Superior chromosome: {best}')





                    