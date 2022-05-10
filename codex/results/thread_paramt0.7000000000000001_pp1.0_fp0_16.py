import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()

import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
from torch.optim import lr_scheduler
from torch.autograd import Variable
from torchvision import datasets, models, transforms

from utils import *

from tqdm import tqdm

import numpy as np
import pickle, os

from collections import OrderedDict

from sklearn.model_selection import train_test_split

from tensorboardX import SummaryWriter


'''
    Train and test the network
'''

if __name__ == '__main__':

    # check if cuda is available
    if torch.cuda.is_available():
        device = torch.device('cuda')
    else:
        device = torch.device('cpu')

    # load model
    model = DeepGaze().to(device)

    # load the data
    with open('../../data/processed/data
