import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()

import os
import time
import numpy as np
import tensorflow as tf
import tensorflow.contrib.slim as slim
import scipy.misc
import scipy.io
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

from utils import *
from ops import *
from tensorflow.examples.tutorials.mnist import input_data

class InfoGAN(object):
    def __init__(self, sess, args):
        self.model_name = 'InfoGAN'
        self.sess = sess
        self.dataset_name = args.dataset
        self.checkpoint_dir = args.checkpoint_dir
        self.result_dir = args.result_dir
        self.log_dir = args.log_dir
        self.epoch = args.epoch
        self.batch_size = args.batch_size
        self.z_dim = args.z_dim
        self.c
