import threading
threading.stack_size(2**27)
import sys
import math

from tensorflow.python.ops import rnn, rnn_cell
from tensorflow.python.ops import variable_scope as vs
from tensorflow.python.ops.math_ops import tanh
from tensorflow.python.ops.math_ops import sigmoid
from tensorflow.python.ops.math_ops import softmax
from tensorflow.python.ops.math_ops import tanh
from tensorflow.python.ops.math_ops import matmul
from tensorflow.python.ops.math_ops import add

from tensorflow.python.ops.nn_ops import relu
from tensorflow.python.ops.nn_ops import sigmoid
from tensorflow.python.ops.nn_ops import softmax
from tensorflow.python.ops.nn_ops import tanh

from tensorflow.python.platform import flags
import numpy as np

from tensorflow.python.ops.gen_math_ops import *

import data_utils
