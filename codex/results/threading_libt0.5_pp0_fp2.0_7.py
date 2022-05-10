import threading
threading.stack_size(67108864)

import sys
import os
import time
import json
import random
import math
import gc
import pickle
import logging
import datetime
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score
from sklearn.preprocessing import MinMaxScaler

import torch
import torch.nn as nn
import torch.utils.data as D
import torch.nn.functional as F
from torch.autograd import Variable
from torch.optim.lr_scheduler import LambdaLR

import warnings
warnings.filterwarnings('ignore')

from tqdm import tqdm_notebook as tqdm

from util import *
from model import *
from dataset import *

# -------------------------
# --- PARAMS
# -------------------------

MODEL_NAME = 'v0'

# -------------------------
# --- INIT
# -------------------------

# init logger
logging.basicConfig(level=
