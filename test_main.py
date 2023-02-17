from simulation import Simulation
from optimizer import Optimizer
import random

# Test case with random parameter ranges
# The test case uses the 1ZoneUncontrolled_win_test.idf model
# The objective is to maximize the average indoor air temperature
param_ranges = {
    'WindowMaterial:SimpleGlazingSystem': {
        'SimpleWindow:DOUBLE PANE WINDOW': {
            'solar_heat_gain_coefficient': [0.25, 0.75],
            'u_factor': [1.0, 2.5]
        }
    }
}

# Create a Simulation object
sim = Simulation('1ZoneUncontrolled_win_test.idf', 'EnergyPlus', param_ranges)

# Perform a random search to find the parameter values that maximize the average indoor air temperature
best_params, best_score = sim.random_search(num_iterations=1000)

# Print the best parameters and score found
print('Best parameters:')
for param, value in best_params.items():
    print(param, value)
print('Best score:', best_score)
