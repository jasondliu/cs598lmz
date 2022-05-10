import ctypes
ctypes.CDLL('./libpython3.7m.so', mode=ctypes.RTLD_GLOBAL)
import sys
sys.path.append('./python')

import argparse
import os
import random
import torch
import torch.nn as nn
import torch.nn.parallel
import torch.backends.cudnn as cudnn
import torch.optim as optim
import torch.utils.data
import torchvision.datasets as dset
import torchvision.transforms as transforms
import torchvision.utils as vutils
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
from IPython.display import HTML
from torch.autograd import Variable

import torchvision.models as models

from PIL import Image

from model import Generator, Discriminator


# Set random seem for reproducibility
manualSeed = 999
#manualSeed = random.randint(1, 10000) # use if you want new results
print("Random Seed: ", manualSeed)
random.seed
