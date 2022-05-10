import mmap
import os
import sys
import time

import numpy as np

import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import torch.utils.data as data

from torch.autograd import Variable
from torch.utils.data.sampler import SubsetRandomSampler

from torchvision import datasets, models, transforms

from PIL import Image

import torch
import torch.nn.functional as F
import torch.nn as nn

import torchvision
from torchvision import models
from torchvision.models.resnet import BasicBlock

#------------------------------------------------------------------------------
# Model
#------------------------------------------------------------------------------

class ResNet18(nn.Module):
    def __init__(self, num_classes, k):
        super(ResNet18, self).__init__()
        self.in_planes = 64
        self.conv1 = nn.Conv2d(3, 64, kernel_size=3, stride=1, padding=1, bias=False)
