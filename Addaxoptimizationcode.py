import numpy as np

def objective_function(x):
    """
    Define your objective function here.
    Example: Sphere function (sum of squares) for minimization.
    """
    return np.sum(x ** 2, axis=1)

def initialize_population(N, dim, lb, ub):
    """Initialize the population randomly within the bounds."""
    return lb + np.random.rand(N, dim) * (ub - lb)

def update_foraging_position(x, best_x, r):
    """Phase 1: Foraging (Exploration)"""
    return x + r * (best_x - x)

def update_digging_position(x, lb, ub, t, T):
    """Phase 2: Digging (Exploitation)"""
    return x + (1 - 2 * np.random.rand(*x.shape)) * ((ub - lb) / (t + 1))

def AOA(N, dim, lb, ub, T):
    """Addax Optimization Algorithm (AOA) implementation."""
    # Step 3: Initialize population
    population = initialize_population(N, dim, lb, ub)
    fitness = objective_function(population)
    
    best_idx = np.argmin(fitness)
    best_x = population[best_idx].copy()
    best_fitness = fitness[best_idx]
    
    # Main optimization loop
    for t in range(1, T + 1):
        for i in range(N):
            r = np.random.rand()
            
            # Foraging phase (Exploration)
            if np.random.rand() < 0.5:
                new_x = update_foraging_position(population[i], best_x, r)
            else:
                # Digging phase (Exploitation)
                new_x = update_digging_position(population[i], lb, ub, t, T)
            
            # Clip to bounds
            new_x = np.clip(new_x, lb, ub)
            new_fitness = objective_function(new_x.reshape(1, -1))[0]
            
            # Update if new solution is better
            if new_fitness < fitness[i]:
                population[i] = new_x
                fitness[i] = new_fitness
                
                # Update best solution found so far
                if new_fitness < best_fitness:
                    best_x = new_x.copy()
                    best_fitness = new_fitness
    
    return best_x, best_fitness

# Example usage
N = 30  # Population size
dim = 5  # Number of variables
lb = np.array([-5] * dim)  # Lower bound
ub = np.array([5] * dim)   # Upper bound
T = 100  # Number of iterations

best_solution, best_value = AOA(N, dim, lb, ub, T)
print("Best solution:", best_solution)
print("Best objective value:", best_value)
