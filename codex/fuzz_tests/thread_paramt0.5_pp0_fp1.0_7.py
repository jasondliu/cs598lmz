import sys, threading
threading.Thread(target=lambda: sys.stdout.write("\x1b[2J\x1b[H"),daemon=True).start()

# Import libs
import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from dlnn.utils.utils import *
from dlnn.utils.utils_plot import *
from dlnn.utils.utils_data import *
from dlnn.utils.utils_model import *
from dlnn.utils.utils_image import *

# Other libs
import numpy as np
import matplotlib.pyplot as plt
import time
from IPython.display import clear_output
from sklearn.metrics import confusion_matrix

# Import PyTorch
import torch
import torch.nn as nn
from torch.autograd import Variable
import torch.nn.functional as F
import torchvision.transforms as transforms
from torch.utils.data import DataLoader
from torch.utils.data.dataset import Dataset

from tensorboardX
