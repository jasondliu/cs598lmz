import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()

import os
import time
import copy
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import DataLoader
import torchvision.transforms as transforms
from torch.autograd import Variable

import torchvision
import torchvision.models as models
from torchvision.models.resnet import BasicBlock
from torchvision.models.vgg import VGG

from dataloader import *
from utils import *
from sklearn.metrics import f1_score as f1

def main(args):
    # Set up network
    if args.model == 'resnet':
        net = ResNet(BasicBlock, [2, 2, 2, 2])
        filepath = os.path.join(args.model_path, args.model + '_' + args.note + '.pth')
    elif args.model == 'vgg16':
        net
