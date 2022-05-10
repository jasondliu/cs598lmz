import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("Python")

import sys
import time
import random
import math
import matplotlib.pyplot as plt

from collections import deque
from operator import itemgetter
from itertools import product, combinations

#------------------------------------------------------------------------------
# Constants
#------------------------------------------------------------------------------

N = 6
M = 3

#------------------------------------------------------------------------------
# Functions
#------------------------------------------------------------------------------

def neighbors(v, n):
    """
    Get the neighbors of a vertex v.
    """
    x = v[0]
    y = v[1]
    return [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]

def valid(v, n):
    """
    Check if a vertex is valid.
    """
    x = v[0]
    y = v[1]
    return 0 <= x < n and 0 <= y < n

def get_edge_weight(v1, v2):
    """
    Get the edge weight.
    """
    return random.random()
