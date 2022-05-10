import ctypes
ctypes.CDLL('libomp.so', mode=ctypes.RTLD_GLOBAL)
import numpy as np
import pandas as pd
import os
import sys
import pathlib
import matplotlib.pyplot as plt

from commai_utils import *

from sklearn.model_selection import train_test_split
from sklearn.utils import shuffle

import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
import torchvision.transforms as T
import torch.utils.data
from torch.utils.data import Dataset, DataLoader

from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.metrics import roc_curve, auc
from sklearn.metrics import confusion_matrix
from sklearn.utils.multiclass import unique_labels

from livelossplot import PlotLosses
from visdom import Visdom

import d
