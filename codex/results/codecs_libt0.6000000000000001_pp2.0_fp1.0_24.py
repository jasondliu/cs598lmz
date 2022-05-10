import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

import os, sys
import numpy as np
import cv2
import math
import getopt
import glob
import matplotlib
# matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pickle
import xml.etree.ElementTree as ET
import time
import torch
import torch.nn as nn
import torch.backends.cudnn as cudnn
import torchvision
import torchvision.transforms as transforms
import torch.optim as optim
import torch.nn.functional as tfunc
from torch.utils.data import Dataset
from torch.utils.data import DataLoader
import torch.optim.lr_scheduler as lr_scheduler

from sklearn.metrics import confusion_matrix
from sklearn.metrics.ranking import roc_auc_score
from sklearn.preprocessing import normalize
from sklearn.metrics import accuracy_score

from PIL import Image
import scipy.
