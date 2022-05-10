import _struct
import time
import math
import itertools

import numpy as np
import matplotlib.pyplot as plt

from IPython.utils import io

from six import print_
from six.moves import xrange

import tensorflow as tf
from tensorflow.python.framework import ops
from tensorflow.python.ops import array_ops
from tensorflow.python.ops import control_flow_ops
from tensorflow.python.ops import embedding_ops
from tensorflow.python.ops import rnn_cell
from tensorflow.python.ops import variable_scope

from tensorflow.python.ops.math_ops import sigmoid
from tensorflow.python.ops.math_ops import tanh

from utils import *

flags = tf.flags
logging = tf.logging

flags.DEFINE_integer("batch_size", None, "Batch size.")
flags.DEFINE_integer("hidden_size", 200, "Size of each model layer.")
flags.DEFINE_integer("num_layers", 1, "
