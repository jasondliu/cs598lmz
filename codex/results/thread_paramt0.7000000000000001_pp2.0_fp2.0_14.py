import sys, threading
threading.Thread(target=lambda: sys.stderr.write('\x1b[2J\x1b[H'),daemon=True).start()

import numpy as np, os, pickle
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
%matplotlib inline
 
from keras.models import Sequential
from keras.layers import Dense, Conv2D, MaxPooling2D, Flatten, Dropout
from keras.optimizers import Adam
from keras.utils.np_utils import to_categorical

import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torchvision import datasets, transforms
from torch.autograd import Variable

import torch

# Set random seed for reproducibility.
seed = 100
np.random.seed(seed)

# Set path to data directory.
data_dir = os.path.join(os.getcwd(),'..','data','poker')

# Set image width and height.
img_width, img_height
