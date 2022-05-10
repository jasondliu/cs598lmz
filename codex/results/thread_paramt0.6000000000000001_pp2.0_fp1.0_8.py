import sys, threading
threading.Thread(target=lambda: sys.stdout.buffer.write(b'\x1b[2J\x1b[H'),daemon=True).start()

import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torchvision import datasets, transforms
from torch.autograd import Variable

import numpy as np
import matplotlib.pyplot as plt

from PIL import Image
import os

import random
import math

import time
import copy

from utils import *

# import warnings
# warnings.filterwarnings("ignore")

import pdb

class Net(nn.Module):
    def __init__(self, input_size, hidden_size, num_classes):
        super(Net, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size) 
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_size, num_classes)  
    
    def forward(self, x
