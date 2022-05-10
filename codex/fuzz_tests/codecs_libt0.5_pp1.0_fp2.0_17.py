import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

import logging
import config
import math
import os
import sys
import random
import re

import numpy as np
import pandas as pd

import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.autograd import Variable

from torch.nn.utils.rnn import pack_padded_sequence, pad_packed_sequence
from torch.nn.utils.rnn import pad_sequence

import torchtext
from torchtext.data import Field, BucketIterator, TabularDataset, Iterator
from torchtext.vocab import Vectors

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

from tqdm import tqdm

from sklearn.metrics import f1_score

# Set random seed
SEED = 2018
random.seed(SEED)
np.random.seed(SE
