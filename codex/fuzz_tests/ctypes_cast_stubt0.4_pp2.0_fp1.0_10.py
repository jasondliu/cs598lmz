import ctypes
ctypes.cast(0, ctypes.py_object).value

# Import modules whose members need to be available in the IPython session.
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Configure some defaults for matplotlib.
%matplotlib inline

from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
 
# Reload all modules imported with %aimport
%load_ext autoreload
%autoreload 1

%aimport helper, tests
from helper import Map, load_map, show_map
from tests import test

%matplotlib inline

map_10 = load_map('map-10.pickle')
show_map(map_10)

map_40 = load_map('map-40.pickle')
show_map(map_40)

# Visualize the paths
path = [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5
