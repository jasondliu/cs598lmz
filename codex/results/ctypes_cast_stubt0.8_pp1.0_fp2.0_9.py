import ctypes
ctypes.cast(0, ctypes.py_object)

# Prevent Numpy from using multiple threads
import os
os.environ['OMP_NUM_THREADS'] = '1'  # export OMP_NUM_THREADS=4
os.environ['OPENBLAS_NUM_THREADS'] = '1'  # export OPENBLAS_NUM_THREADS=4
os.environ['MKL_NUM_THREADS'] = '1'  # export MKL_NUM_THREADS=6
os.environ['VECLIB_MAXIMUM_THREADS'] = '1'  # export VECLIB_MAXIMUM_THREADS=4
os.environ['NUMEXPR_NUM_THREADS'] = '1'  # export NUMEXPR_NUM_THREADS=6

from graphviz import Source
import matplotlib.animation as animation
import matplotlib.cm as cm
from matplotlib.colors import ListedColormap, LinearSegmentedColormap

"""
Auxiliary functions
"""


def size
