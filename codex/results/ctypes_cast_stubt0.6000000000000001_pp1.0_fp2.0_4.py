import ctypes
ctypes.cast(None, ctypes.py_object)

import numpy as np
import pandas as pd
import os
import sys
import shutil
import random
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.preprocessing import StandardScaler
from sklearn.utils.multiclass import unique_labels

import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import Dataset, DataLoader, random_split

# Load data
data = pd.read_csv('../data/processed/train.csv')
#data = pd.read_csv('../data/processed/train_sample.csv')

# Split into validation and training set
train_set, val_set = train_test_split(data, test_size=0.2, random_state=42)

# Create data loaders
batch_size = 512

# Sh
