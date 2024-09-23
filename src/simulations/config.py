seed = 123456

param_bounds = {
    'S': [500, 1000],
    'sigma': [0.1, 1],
    'tau': [14/252, 2],
    'r': [0.1/100, 5/100],
}

strikes_per_S = 4

sample_sizes = [5_000, 10_000, 20_000, 50_000, 100_000, 200_000]

path_to_data = 'data/simulated/simulation_1.csv'