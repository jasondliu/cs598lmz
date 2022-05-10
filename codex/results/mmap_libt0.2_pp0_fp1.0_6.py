import mmap
import numpy as np
import os
import pandas as pd
import re
import sys
import time
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.autograd import Variable
from torch.utils.data import Dataset, DataLoader
from tqdm import tqdm

from utils import *

# Set random seed
torch.manual_seed(1)

# Set device
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

# Set data path
data_path = '../data/'

# Set model path
model_path = '../model/'

# Set output path
output_path = '../output/'

# Set batch size
batch_size = 128

# Set embedding size
embedding_size = 300

# Set hidden size
hidden_size = 256

# Set number of layers
num_layers = 1

# Set dropout
dropout = 0.5

#
