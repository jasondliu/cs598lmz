import types
types.ModuleType.__repr__ = lambda self: self.__name__

import sys
sys.path.append('../')

import numpy as np
import matplotlib.pyplot as plt

from src.utils import *
from src.data import *
from src.model import *
from src.metrics import *
from src.visualization import *

from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.utils.data import DataLoader
from torch.utils.data import sampler

import time

# Set random seed
seed = 1
np.random.seed(seed)
torch.manual_seed(seed)

# Set device
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

# Load data
X_train, y_train, X_test, y_test = load_data()

# Split
