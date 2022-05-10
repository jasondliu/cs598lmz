import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)
import logging
import os
import sys
import argparse
from argparse import RawTextHelpFormatter

import numpy as np
import pandas as pd
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
import torch.nn.functional as F

from utils.utils import fix_seeds
from utils.tokenizer import Tokenizer
from utils.data import load_data, load_data_for_inference
from models.tree_lstm import TreeLSTM

# The following codes are from https://github.com/allenai/allennlp/blob/master/allennlp/nn/util.py
def add_sentence_boundary_token_ids(tokens, mask, sentence_begin_token='<s>', sentence_end_token='</s>',
                                    data_parallel=False,
                                    device=-1):
    """
    This
