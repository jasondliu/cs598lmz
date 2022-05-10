from lzma import LZMADecompressor
LZMADecompressor().decompress(b'\x00')

# (The above line is just to check that the LZMADecompressor class is available.)

# In[4]:

# get_ipython().run_line_magic('pylab', 'inline')
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

# In[5]:

# from IPython.display import display

# In[6]:

import os
import sys
import gc
import time
import random
import pickle

# import warnings
# warnings.filterwarnings('ignore')

# In[7]:

import numpy as np
import pandas as pd

# In[8]:

import multiprocessing as mp

# In[9]:

from tqdm import tqdm, tqdm_notebook

# In[10]:

import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import DataLoader, Dataset

# In[
