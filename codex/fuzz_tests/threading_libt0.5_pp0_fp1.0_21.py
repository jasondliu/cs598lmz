import threading
threading.stack_size(67108864)

import sys
sys.path.insert(0, '../../src/')

import numpy as np
import matplotlib.pyplot as plt
import os
import pickle
import time
import pdb

from utils import *

from scipy.optimize import minimize
from scipy.optimize import Bounds
from scipy.optimize import LinearConstraint
from scipy.optimize import SR1
from scipy.optimize import BFGS

from sklearn.preprocessing import StandardScaler

# Define the dimensions of the problem
n_inputs = 1
n_outputs = 1

# Define the number of samples
n_samples = 10

# Define the number of training iterations
n_iter = 100000

# Define the activation function
activation_function = 'relu'

# Define the output noise
noise = 0.05

# Define the number of neurons per layer
n_neurons_1 = 10
n_neurons_2
