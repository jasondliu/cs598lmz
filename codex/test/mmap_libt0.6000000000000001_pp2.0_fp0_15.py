import mmap
import numpy as np
import sys
import torch
import random
from torch.utils.data import Dataset, DataLoader
import torch.nn as nn
import torch.nn.functional as F
from torch.autograd import Variable
import torch.optim as optim
import pickle
from collections import Counter
import time
from tqdm import tqdm
from sklearn.metrics import f1_score

from util import *
from model import *


#set random seed
seed = 1
torch.manual_seed(seed)
np.random.seed(seed)
random.seed(seed)
torch.backends.cudnn.deterministic=True

#set hyperparameters
n_vocab = 25000
#n_vocab = 20000
n_embedding = 100
n_hidden = 100
n_tag = 19
n_epoch = 10
n_batch = 32
lr = 0.001

#load data
