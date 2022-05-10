import ctypes
ctypes.windll.user32.SetProcessDPIAware()

import sys
import os
import json
import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.widgets import Button

import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
from torchvision import datasets, transforms

from PIL import Image

from sklearn.metrics import confusion_matrix, roc_curve, auc
from sklearn.model_selection import train_test_split

from tqdm import tqdm
from time import time

from utils import *
from models import *
from dataset import *

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

def main():
    # load data
    print('Loading data...')
    data_dir = 'data/'
    img_dir = data_dir + '
