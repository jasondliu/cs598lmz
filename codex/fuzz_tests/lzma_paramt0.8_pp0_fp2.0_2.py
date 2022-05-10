from lzma import LZMADecompressor
LZMADecompressor().decompress(open('data/char2id.dict.gz','rb').read())


import numpy as np
import pandas as pd

import gzip
import json
import pickle

import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_recall_fscore_support

import matplotlib.pyplot as plt
import seaborn as sns

sns.reset_defaults()
sns.set_context(context='talk',font_scale=0.7)

import warnings
warnings.filterwarnings('ignore')

import json
import re
import string

from tqdm import tqdm
tqdm.pandas
