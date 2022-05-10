import threading
threading.stack_size(1024*1024*1024)

import sys
sys.path.append('../')
import os
import time
import logging
import argparse
import datetime
import numpy as np
from tqdm import tqdm
import torch
import torch.nn as nn
import torch.optim as optim
from torch.autograd import Variable
from torch.optim.lr_scheduler import ReduceLROnPlateau
import torch.nn.functional as F

from utils.utils import *
from utils.logger import Logger
from utils.data_loader import DataLoader
from utils.data_loader_test import DataLoaderTest
from utils.data_loader_test_val import DataLoaderTestVal
from utils.data_loader_val import DataLoaderVal
from models.net import Net
from models.net_res import NetRes


parser = argparse.ArgumentParser(description='PyTorch Training')
parser.add_argument('--model', default='res', type=str, help='model')
