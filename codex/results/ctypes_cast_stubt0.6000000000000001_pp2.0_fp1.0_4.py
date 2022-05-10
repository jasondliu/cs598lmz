import ctypes
ctypes.cast(0, ctypes.py_object)

# imports
import sys
import os
import random
import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from itertools import combinations
import csv

# set seed
random.seed(42)
np.random.seed(42)

# local modules
if os.path.basename(os.getcwd()) == "tests":
    sys.path.append(os.path.join(os.path.dirname(os.getcwd()), "source"))

if os.path.basename(os.getcwd()) == "moabb":
    sys.path.append(os.path.join(os.path.dirname(os.getcwd()), "..", "tests", "source"))

from functions import *
from plotting import *

# matplotlib
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

matplotlib.rcParams['pdf.fonttype'] = 42
