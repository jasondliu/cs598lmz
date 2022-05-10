import ctypes
ctypes.windll.user32.SetProcessDPIAware()

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np

# Create a Random Number Generator with a seed, important for creating the same "random" data every time
import random
seed = 12345
np.random.seed(seed)
random.seed(seed)

# Import some functionality from scikit-image
from skimage import data, color, exposure, img_as_float, img_as_ubyte

# Import functionality for PCA
from sklearn.decomposition import PCA


def normalize(x):
    """Normalize data x to have zero-mean and unit variance"""
    return (x-np.mean(x))/np.std(x)

def get_positive_part(x):
    """Calculate x_+ = max(x,0)"""
    return np.maximum(x, np.zer
