import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import KFold

import torch
import torch.nn as nn
from torch.nn import functional as F
import torch.optim as optim
from torch.utils.data import DataLoader, Dataset
from torch.utils.data.sampler import RandomSampler, SequentialSampler
from torch.nn.utils.rnn import pad_sequence
from torch.autograd import Variable
from torch.optim.lr_scheduler import _LRScheduler
from tqdm.autonotebook import tqdm

from pytorch_pretrained_bert import BertTokenizer
from pytorch_pretrained_bert import BertAdam
from pytorch_pretrained_bert
