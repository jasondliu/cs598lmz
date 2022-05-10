import codecs
codecs.register_error('strict', codecs.ignore_errors)

import os
import sys
import re
import argparse
import json
from collections import Counter

import torch
from torch.utils.data import DataLoader
from torch.autograd import Variable
from torch import nn
from torch import optim
from torch.nn import functional as F

from lib.utils import *
from lib.dataset import *
from lib.model import *
from lib.trainer import *

from lib.metric import *

from nltk.tokenize import TweetTokenizer

from sklearn.metrics import f1_score
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score

from sklearn import metrics

from nltk.tokenize import TweetTokenizer

from sklearn.metrics import confusion_matrix

from sklearn.metrics import classification_report

from sklearn.metrics import make_scorer

from sklearn.metrics import roc_auc_score

from sklearn.met
