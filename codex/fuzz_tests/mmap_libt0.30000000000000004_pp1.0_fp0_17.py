import mmap
import numpy as np
import os
import pickle
import re
import scipy.sparse
import scipy.sparse.linalg
import sys
import time
import traceback

from collections import defaultdict
from datetime import datetime
from itertools import islice
from multiprocessing import Pool, cpu_count
from os.path import join as path_join
from sklearn.metrics import roc_auc_score
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import normalize
from sklearn.utils import shuffle

from utils import *

#-------------------------------------------------------------------------------
# Globals
#-------------------------------------------------------------------------------

# Paths
DATA_DIR = 'data'

# Data
NUM_USERS = 458293
NUM_MOVIES = 17770

#-------------------------------------------------------------------------------
# Functions
#-------------------------------------------------------------------------------

def get_data(filename):
    """
    Reads in data from a file and returns a list of tuples.
    """
    data = []
    with open(filename, 'r') as f
