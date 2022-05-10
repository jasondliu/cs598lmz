import lzma
lzma.MAX_MEM_COMP = 1000
import sys
import os
import time
import matplotlib.pyplot as plt
import numpy as np
from numpy import linalg as LA

from sklearn.datasets import fetch_olivetti_faces
from sklearn.utils.validation import check_random_state

from sklearn.ensemble import ExtraTreesRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import RidgeCV
from sklearn.ensemble import AdaBoostRegressor
from sklearn.ensemble import RandomForestRegressor

from sklearn.feature_extraction.image import grid_to_graph
from sklearn.decomposition import PCA

import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim


# In[2]:


def fetch_batch(batch_size=64, resolution=64, compress_factor=2, test=False, batch_no=0):
    path =
