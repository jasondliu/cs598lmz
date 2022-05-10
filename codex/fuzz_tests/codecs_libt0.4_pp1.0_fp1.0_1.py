import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'cp65001' else None)

import os
import sys
import json
import time
import argparse
import numpy as np
import tensorflow as tf
from tqdm import tqdm

from model import Model
from util import load_data, load_word_vec, get_minibatches, sample
from rouge import Rouge

parser = argparse.ArgumentParser()
parser.add_argument('--data_dir', type=str, default='data/cnndm')
parser.add_argument('--train_dir', type=str, default='data/cnndm')
parser.add_argument('--mode', type=str, default='train')
parser.add_argument('--batch_size', type=int, default=32)
parser.add_argument('--use_buckets', type=bool, default=False)
parser.add_argument('--bucket_interval', type=int, default=10)
parser.add_argument('--max_enc_steps', type=int
