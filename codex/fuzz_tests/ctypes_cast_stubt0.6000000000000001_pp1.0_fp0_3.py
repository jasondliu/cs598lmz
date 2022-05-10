import ctypes
ctypes.cast(0, ctypes.py_object).value = None

# In[3]:

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.patches import Rectangle
from matplotlib.collections import PatchCollection
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.colors import Normalize
from matplotlib.cm import ScalarMappable
from matplotlib import animation
import matplotlib.cm as cm
import time
import sys
import os
import h5py
import glob
import warnings
#warnings.filterwarnings("ignore")

# In[4]:

#import matplotlib.style
#matplotlib.style.use('ggplot')

# In[5]:

#from matplotlib import rc
#rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
## for Palatino and other serif fonts use:
#rc('font',**{'family
