import select_data
import os
import numpy as np
import scipy.stats as st

def save_data(filename, data):
    np.savetxt(filename, data, fmt='%s', delimiter=',')
    return True

def get_data(data, stat):
    if stat == 'mean':
        return np.mean(data)
    elif stat == 'median':
        return np.median(data)
    elif stat == 'mode':
        return st.mode(data)[0][0]
    elif stat == 'var':
        return np.var(data)
    elif stat == 'std':
        return np.std(data)
    elif stat == 'min':
        return np.min(data)
    elif stat == 'max':
        return np.max(data)
    else:
        return 'Error'

def get_stats(data, stat, save_fname):
    data_stats = []
    for d in data:
        data_stats.append(get_data(d, stat))

