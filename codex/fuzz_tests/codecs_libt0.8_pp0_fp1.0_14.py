import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

import os
import sys
sys.path.append('..')
from config import load_config
from utils import load_pkl, save_pkl, prepare_dir
from data_utils import prepare_embed_table
from model_utils import get_model, get_optimizer, get_scheduler
from metrics import get_fmeasure
from data_loader import SentenceRELoader
from tensorboardX import SummaryWriter

import torch
import time
import random
import argparse
import numpy as np


def set_seed(args):
    random.seed(args.seed)
    np.random.seed(args.seed)
    torch.manual_seed(args.seed)
    if args.cuda:
        torch.cuda.manual_seed_all(args.seed)


def save_checkpoint(state, is_best, fpath='checkpoint.pt'):
    """Saves checkpoint to disk"""
    torch.save(
