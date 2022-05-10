import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)
import sys
import collections
import copy

import matplotlib.pyplot as plt
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as torchfunc
from torch.autograd import Variable
import torch.optim as optim
import torch.utils.data as data
from sklearn.metrics import f1_score
import time
from torchcrf import CRF 
from nltk.tag import ClassifierBasedTagger

#sys.path.append('/Users/jgarcia/Projects/semeval2020-multimodal-emotion-detection/multimodal-cde-master/multimodal_cde')
sys.path.append('.')
from io_utils import *
from data_utils import *
from core import *
from train_utils import *

from torchcrf import CRF 
from nltk.tag import ClassifierBasedTagger
from sklearn.svm import LinearSVC, SVC

