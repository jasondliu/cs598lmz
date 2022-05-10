import ctypes
ctypes.cast(None, ctypes.c_void_p)

import torch
import torch.nn as nn
from torch.autograd import Variable
from torch.utils.data import DataLoader
from torch.utils.data.sampler import SubsetRandomSampler

from data_loader import *
from models import *
from utils import *

if torch.cuda.is_available():
    dtype = torch.cuda.FloatTensor
else:
    dtype = torch.FloatTensor

'''
    Set up all the directories
'''
data_dir = 'data'
model_dir = 'models'

# Create directories if they don't exist
if not os.path.exists(data_dir):
    os.makedirs(data_dir)
if not os.path.exists(model_dir):
    os.makedirs(model_dir)

'''
    Hyperparameters
'''
num_epochs = 100
batch_size = 64
learning_rate = 0.001
num_workers = 0

'''
    Load the
