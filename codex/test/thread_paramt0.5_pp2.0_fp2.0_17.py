import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()

# %matplotlib inline

# from IPython.core.display import display, HTML
# display(HTML("<style>.container { width:100% !important; }</style>"))

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# import random
# import math
# import time
# import datetime

import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.autograd import Variable
from torch.distributions import Categorical

import gym
import gym_maze

# plt.rcParams['figure.figsize'] = [20, 10]
# plt.rcParams['figure.dpi'] = 200

print(torch.__version__)

use_cuda = torch.cuda.is_available()
# use_cuda = False

FloatTensor = torch.cuda.FloatT
