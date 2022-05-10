import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_double)

import sys
import csv
import os.path
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import  matplotlib.cm as cm
import numpy as np
import math
import copy as copy

sys.path.append('../../scripts')
from pareto_frontier_2D import pareto_frontier
from pareto_frontier_2D_answer import pareto_frontier_answer

###
# this script make the figure showing the initial pareto frontier
###

def pareto_frontier_sw(x_values, y_values):
	x_values = np.array(x_values)
	y_values = np.array(y_values)
	
	# Sort the list in either ascending or descending order of X
	sorted_list = sorted(zip(x_values
