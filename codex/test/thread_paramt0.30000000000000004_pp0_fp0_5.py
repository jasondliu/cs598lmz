import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from mpl_toolkits.mplot3d import Axes3D

from IPython.display import HTML

import torch
from torch import nn
from torch.nn import functional as F
from torch.autograd import Variable
from torch.utils.data import Dataset, DataLoader

from torchvision import transforms, datasets

import torchvision.models as models

import torch.optim as optim

import os
import time

import copy

import cv2

from PIL import Image

from sklearn.metrics import confusion_matrix

import pandas as pd

import seaborn as sn

from tqdm import tqdm

from sklearn.metrics import confusion_matrix

import random

from sklearn.metrics import confusion_matrix

from sklearn.metrics import classification_report

