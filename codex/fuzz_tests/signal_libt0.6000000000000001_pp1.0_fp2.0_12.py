import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import os
import sys
import argparse
import logging
import tensorflow as tf
import numpy as np
import random
import time

import utils
import tf_utils

# Constants

# Default values for some parameters
DEFAULT_BATCH_SIZE = 16
DEFAULT_EPOCHS = 2000

# Set random seeds for reproducibility
SEED = 42
np.random.seed(SEED)
random.seed(SEED)

# Arguments

parser = argparse.ArgumentParser(description='Train a model')

# Data
parser.add_argument('--dataset', type=str, required=True,
                    help='Dataset to use')
parser.add_argument('--dataset_dir', type=str, required=True,
                    help='Directory containing the dataset')
parser.add_argument('--input_size', type=int, default=64,
                    help='Size of input images (width and height)')
parser.add_argument
