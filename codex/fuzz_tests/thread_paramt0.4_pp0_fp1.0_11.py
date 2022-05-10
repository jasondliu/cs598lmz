import sys, threading
threading.Thread(target=lambda: sys.stdout.write("\n")).start()

import os
import time
import random
import datetime
import argparse
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.autograd import Variable
from torch.utils.data import DataLoader
from torch.utils.data import TensorDataset
from torch.utils.data.sampler import SubsetRandomSampler
from torchvision import datasets, transforms
from scipy.stats import norm
from scipy.stats import multivariate_normal
from sklearn.model_selection import train_test_split
from sklearn.utils import shuffle

from vae_models import *
from vae_utils import *
from vae_datasets import *
from vae_options import *

# -----------------------------------------------------------------------------
# Options
# -----------------------------------------------------------------------------
parser = argparse.ArgumentParser()
parser = add_vae_args(parser)
args = parser.parse_args()

# -----------------------------------------------------------------------------
# Set options
# -----------------------------------------------------------------------------


