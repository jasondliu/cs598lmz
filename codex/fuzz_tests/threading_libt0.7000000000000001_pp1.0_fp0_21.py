import threading
threading.stack_size(1024*1024*40)

import os, sys, time
from PIL import Image
import numpy as np

sys.path.append('../')
import utils.logger as logger
import utils.utils as utils
import utils.dataloader as dataloader
import utils.config as config

# import utils.logger as logger
# import utils.utils as utils
# import utils.dataloader as dataloader
# import utils.config as config

import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.autograd import Variable

import torchvision
import torchvision.datasets as datasets
import torchvision.transforms as transforms

import torch.optim as optim
from torch.optim import lr_scheduler

from model.basemodel import basemodel
from train import train
import argparse

parser = argparse.ArgumentParser(description='Training code')
parser.add_argument('--model_name', default='resnet
