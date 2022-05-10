import mmap
import os
import re
import sys
import time
from collections import defaultdict
from datetime import datetime
from subprocess import Popen, PIPE

import numpy as np
import pandas as pd
from scipy.stats import entropy
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score

from utils import *

# Set random seed
np.random.seed(42)

# Set global variables
# Paths
DATA_DIR = 'data'
MODEL_DIR = 'models'

# Data
TRAIN_FILE = 'train.csv'
TEST_FILE = 'test.csv'

# Model
MODEL_NAME = 'model.h5'

# Training
BATCH_SIZE = 128
EPOCHS = 10

# Testing
TEST_BATCH_SIZE = 128

# Evaluation
EVAL_BATCH_SIZE = 128

# Logging
LOG_FILE = 'log.txt'

# Set global variables
# Paths
DATA_DIR = 'data'

