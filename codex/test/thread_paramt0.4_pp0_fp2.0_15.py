import sys, threading
threading.Thread(target=lambda: sys.stdout.write("\x1b[2J\x1b[H"),daemon=True).start()

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation

import time

# from IPython import display

# from IPython.display import clear_output
# from matplotlib import pyplot as plt
# %matplotlib inline

import gym

import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

from torch.distributions import Categorical

# if gpu is to be used
use_cuda = torch.cuda.is_available()
device   = torch.device("cuda" if use_cuda else "cpu")

