import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()

import os
import time
import numpy as np
import tensorflow as tf

import sys
sys.path.append('../')
import utils.utils as utils
import utils.model as model
import utils.data as data

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--name', type=str, default='model')
parser.add_argument('--gpu', type=str, default='0')
parser.add_argument('--dataset', type=str, default='cifar10')
parser.add_argument('--batch_size', type=int, default=100)
parser.add_argument('--epochs', type=int, default=200)
parser.add_argument('--lr', type=float, default=0.1)
parser.add_argument('--momentum', type=float, default=0.9)
parser.add_argument('--decay', type=float, default=0.0001)
parser.add_argument('
