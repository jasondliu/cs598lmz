import threading
threading.stack_size(67108864)

#import matplotlib.pyplot as plt
#import numpy as np

def main():
    #defining the problem
    #problem = tsp.TSP_Problem(100, 10)
    #problem.create_problem(3, 3)
    problem = tsp.TSP_Problem(50, 10)
    problem.create_problem(4, 4)
    #problem = tsp.TSP_Problem(500, 100)
    #problem.create_problem(10, 10)
    #problem = tsp.TSP_Problem(1000, 1000)
    #problem.create_problem(5, 5)
    #problem = tsp.TSP_Problem(50, 10)
    #problem.create_problem(10, 10)
    #problem = tsp.TSP_Problem(100, 10)
    #problem.create_problem(3, 3)
    problem.print_problem()

    #creating the population
    population = tsp.Population(50, problem)

    #seeding the population
    population.seed()


