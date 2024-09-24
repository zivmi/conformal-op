import numpy as np
import pandas as pd
from scipy.stats import norm

import sys
sys.path.append('.')

from config import * 
from src.utils.common import d1, d2, black_scholes_price

if __name__ == '__main__':
    total_num_samples = int(sum(sample_sizes)/strikes_per_S)

    # generate data from uniform distribution for each parameter
    np.random.seed(seed)
    data = {}
    for param in param_bounds.keys():
        data[param] = np.repeat( # repeat the same sampled value strikes_per_S times
            np.random.uniform(
                param_bounds[param][0], # lower bound
                param_bounds[param][1], # upper bound 
                total_num_samples), 
            strikes_per_S)

    # generate 'strikes_per_S' number of strikes from normal with mean S and std 0.1*S, for each S
    z = np.random.normal(
            1, # mean
            # variance of 0.1 => std=sqrt(0.1)=0.316
            # ~300 strikes will be negative
            # the author probably used 0.1 as a variance, not std.
            # With std=0.1, the number of negative strikes will be ~0
            0.1, 
            total_num_samples*strikes_per_S)

    data['K'] = data['S']/z

    data = pd.DataFrame(data)

    # Label the samples with the sample id, according to the sample_sizes list.
    # This will make it easier to split dataframe into samples of different sizes.
    data['sample_id'] = 0
    for i, _ in enumerate(sample_sizes):
        data.loc[data.index.isin(range(sum(sample_sizes[:i]), sum(sample_sizes[:i+1]))), 'sample_id'] = i

    # Add the option price
    data['C'] = black_scholes_price(data['S'], data['K'], data['r'], data['sigma'], data['tau'], option_type="call")

    # Save the data to a csv file
    data.to_csv(path_to_data, index=False)