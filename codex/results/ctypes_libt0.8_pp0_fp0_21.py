import ctypes
ctypes.windll.user32.SetProcessDPIAware()

import numpy as np
from scipy.io import savemat
from matplotlib import pyplot as plt

import sys
sys.path.append('../compute_tools')
from compute_tools import *

import os
# os.environ["CUDA_DEVICE_ORDER"]="PCI_BUS_ID"
# os.environ["CUDA_VISIBLE_DEVICES"]="0"

import tensorflow as tf
from sklearn.utils import shuffle
from tensorflow.python.ops import math_ops
from tensorflow.python.ops import random_ops
from tensorflow.python.ops import array_ops
from tensorflow.python.framework import ops
from tensorflow.python.framework import dtypes
from tensorflow.python.ops import nn
from tensorflow.python.ops import nn_ops
from tensorflow.python.ops import variable_scope
from tensorflow.python.training import moving_averages

import scipy.io as sio


