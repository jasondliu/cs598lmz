import mmap
import numpy as np
# import re
import time
import os
import sys
import torch
import warnings
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import torch.optim.lr_scheduler as lr_scheduler
from torch.utils.data import DataLoader, Dataset
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import model_selection, preprocessing
# from sklearn.metrics import precision_recall_curve
from sklearn.metrics import accuracy_score, auc, classification_report, roc_auc_score
import matplotlib.pyplot as plt
from collections import Counter
from gensim.models import Word2Vec
import random

#os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
#os.environ["CUDA_VISIBLE_DEVICES"] = "0,1,2,3"

warnings.filterwarnings('ignore')
# torch.multiprocessing.
