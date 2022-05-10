import mmap
from math import log
import pickle
import sys
from sklearn.metrics import mean_squared_error
import argparse

parser = argparse.ArgumentParser(description='Finds the best lmbda value for the given dataset.')
parser.add_argument('train_data', help='File containing the training data')
parser.add_argument('test_data', help='File containing the test data')
parser.add_argument('output_file', help='File in which to store the output')
parser.add_argument('-f', '--features', type=int, default=50, help='Number of features to use')
parser.add_argument('-l', '--lmbda', type=float, default=0.001, help='Lmbda value to use')

args = parser.parse_args()

# The number of features to use
FEATURES = args.features

# The lambda value to use
LMBDA = args.lmbda

# The training data file
TRAIN_DATA_FILE = args.train_data

# The test data file
T
