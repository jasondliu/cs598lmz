import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patches as patches
from matplotlib.collections import PatchCollection

import time
import math

import random

#import pdb

#import pydevd
#pydevd.settrace('localhost', port=51234, stdoutToServer=True, stderrToServer=True)

#import pdb; pdb.set_trace()

#--------------------------------------------------------------------------------------------------

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt(math.pow(x1-x2, 2) + math.pow(y1-y2, 2))

#--------------------------------------------------------------------------------------------------

def get_distance_matrix(x, y):
    distance_matrix = np.zeros((len(x), len(x)))
    for i in range(len
