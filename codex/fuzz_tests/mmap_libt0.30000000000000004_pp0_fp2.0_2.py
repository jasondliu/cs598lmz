import mmap
import numpy as np
import os
import re
import sys

from collections import defaultdict
from scipy.sparse import csr_matrix
from sklearn.utils import murmurhash3_32

from . import constants, utils

def _get_data_path():
    return os.path.join(os.path.dirname(__file__), 'data')

def _get_model_path():
    return os.path.join(os.path.dirname(__file__), 'models')

def _get_word_set_path():
    return os.path.join(_get_data_path(), 'word_set.txt')

def _get_word_set_mmap_path():
    return os.path.join(_get_data_path(), 'word_set.mmap')

def _get_word_set_mmap_path_tmp():
    return os.path.join(_get_data_path(), 'word_set.mmap.tmp')

def _get_word_set_mmap_path_lock():
