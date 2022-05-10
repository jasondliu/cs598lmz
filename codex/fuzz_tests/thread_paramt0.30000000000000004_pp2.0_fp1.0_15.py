import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()

import os
import time
import numpy as np
import tensorflow as tf
import tensorflow.contrib.slim as slim
from tensorflow.python.ops import control_flow_ops
from tensorflow.python.training import moving_averages

from config import cfg
from utils import *
from ops import *
from datasets import *
from nets import *

def main():
    if not os.path.exists(cfg.LOG_DIR):
        os.makedirs(cfg.LOG_DIR)
    if not os.path.exists(cfg.MODEL_DIR):
        os.makedirs(cfg.MODEL_DIR)
    if not os.path.exists(cfg.SAMPLE_DIR):
        os.makedirs(cfg.SAMPLE_DIR)

    # Load dataset
    print('Loading dataset...')
    dataset = load_dataset(cfg.DATASET)
    print('Finished loading dataset')

    # Build model
    print('Building model
