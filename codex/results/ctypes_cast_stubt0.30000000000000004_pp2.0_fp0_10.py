import ctypes
ctypes.cast(0, ctypes.py_object)

#import os
#os.environ["PYTHONSTARTUP"] = "~/.pythonrc"

import sys
sys.ps1 = '\033[1;32m>>> \033[0m'
sys.ps2 = '\033[1;32m... \033[0m'

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import warnings
warnings.filterwarnings('ignore')

#from IPython.core.interactiveshell import InteractiveShell
#InteractiveShell.ast_node_interactivity = "all"

#from IPython.display import display
#pd.options.display.max_columns = None
#pd.options.display.max_rows = None

import matplotlib as mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['font.family'] = 'sans-serif'
mpl.rcPar
