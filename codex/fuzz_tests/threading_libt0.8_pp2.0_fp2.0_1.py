import threading
threading._DummyThread._Thread__stop = lambda x: 42

import sys
import argparse
import csv
import re
import os

from tensorboardX import SummaryWriter
import torch
import torch.nn as nn
import torch.nn.utils
import torch.nn.functional as F
import torch.optim as optim
from torch.autograd import Variable
from torch.utils.data import DataLoader, TensorDataset
from torch.nn.utils.rnn import pack_padded_sequence
from tqdm import tqdm

import util
'''TODO:
    1. Implement __len__()
    2. Implement __getitem__()
    3. Implement __init__()
'''
# class IMDBDataset(torch.utils.data.Dataset):
#     def __len__(self):
#         pass
#     def __getitem__(self, idx):
#         pass
#     def __init__(self, text_path, label_path, vocab):
#         with open(text_path, 'r') as
