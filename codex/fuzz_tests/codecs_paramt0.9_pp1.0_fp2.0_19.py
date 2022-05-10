import codecs
codecs.register_error('replace_with_space', lambda e: (u' ',e.start + 1))
# from Article in https://github.com/dyckias/BabyMonitor/blob/master/other_files/gen_files.py
import os
import sys
import random

# from NMT
import torch
import torch.nn as nn
from torch import optim
import torch.nn.functional as F
import logging
import tempfile
# change this class

device = torch.device("cuda:0")

# Ignore warnings
import warnings
warnings.filterwarnings("ignore")

'''
  The following classes are used to preprocess the data. 

  The overall NMT task is split into three steps:
  (1) Read in the sentence pairs,
  (2) Convert the words in the sentence pairs to indices, and
  (3) Create batches to make training efficient.

  Each step of the data pipeline is handled by one of the following classes:
  (1) Voc - a vocabulary that reads, stores and converts words into indices
  (2) LanguageIndexer - a helper class to create a language
