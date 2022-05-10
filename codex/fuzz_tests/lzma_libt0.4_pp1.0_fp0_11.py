import lzma
lzma.LZMAFile

import os
import pickle
import sys
import time
import urllib.request

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
%matplotlib inline

import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import torch.utils.data

from torch.utils.data import Dataset, DataLoader
from torchvision import transforms, utils

from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score

from tqdm import tqdm_notebook

from IPython.display import clear_output

import warnings
warnings.filterwarnings('ignore')

from google.colab import drive
drive.mount('/content/drive')

device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')

# всегда фиксируйте
