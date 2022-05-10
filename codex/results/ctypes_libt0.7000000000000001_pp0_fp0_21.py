import ctypes
ctypes.CDLL('/usr/lib/x86_64-linux-gnu/libXrender.so.1', mode=ctypes.RTLD_GLOBAL)

import matplotlib.pyplot as plt
# import seaborn as sns
# from matplotlib.ticker import MaxNLocator
from matplotlib.patches import Rectangle
# from matplotlib.collections import PatchCollection
from matplotlib.collections import LineCollection
import numpy as np
# from load_data import load_data
# from load_data import load_data_wide
# import seaborn as sns
import pickle
import os
import argparse
import time
import math
# from matplotlib.colors import ListedColormap
# import tqdm

# args = parser.parse_args()
# saving_path = args.saving_path
# data_path = args.data_path

# saving_path = '/home/ngaude/workspace/data/lm/'
# data_path = '/home/ngaude/workspace/data/
