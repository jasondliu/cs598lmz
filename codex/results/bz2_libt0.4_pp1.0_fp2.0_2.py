import bz2
bz2.BZ2File

import sys
sys.path.append('../')

from utils.utils import *
from utils.model_utils import *
from utils.plot_utils import *
from utils.data_utils import *
from model.model import *
from model.model_resnet import *

import tensorflow as tf
from tensorflow.python.framework import ops
from tensorflow.python.ops import clip_ops
from tensorflow.python.ops import math_ops
from tensorflow.python.ops import nn_ops
from tensorflow.python.ops import array_ops
from tensorflow.python.ops import init_ops
from tensorflow.python.ops import variable_scope as vs
from tensorflow.python.training import moving_averages

import os
import time
import numpy as np
import random
import pickle
import matplotlib.pyplot as plt
import argparse
from collections import defaultdict
from scipy.stats import pearsonr
from sklearn.metrics import r2_score

from
