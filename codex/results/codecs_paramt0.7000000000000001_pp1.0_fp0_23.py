import codecs
codecs.register_error('surrogate_escape', codecs.lookup_error('ignore'))

import os
import time
import datetime
import re

from random import seed
from random import randint

import pandas as pd
from tqdm import tqdm
from nltk import ngrams
from nltk.corpus import stopwords 
import numpy as np
import torch
from torch import nn
from torch import optim
import torch.nn.functional as F
from torch.utils.data import Dataset, DataLoader
import torch
from pytorch_pretrained_bert import BertTokenizer, BertAdam, BertModel
from pytorch_pretrained_bert.modeling import BertPreTrainedModel, BertModel, BertConfig
from sklearn.metrics import f1_score, accuracy_score
import pickle

from util import *
from model import *

from torch.nn.utils.rnn import pad_sequence, pack_padded_sequence, pad_packed_sequence


from sklearn.model_selection import KFold

from utils import clean_text,
