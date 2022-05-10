import _struct
import sys
import time

import numpy as np
import scipy.io.wavfile

import chime_utilities as utils

import tensorflow as tf
from tensorflow.python.ops import variable_scope as vs

from tensorflow.python.ops import rnn_cell
from tensorflow.python.ops import rnn

from tensorflow.python.ops import math_ops
from tensorflow.python.ops import array_ops
from tensorflow.python.ops import variable_scope

from tensorflow.python.ops import init_ops
from tensorflow.python.ops import nn_ops

from tensorflow.python.ops import control_flow_ops

from tensorflow.python.util import nest

from tensorflow.python.ops import embedding_ops

from tensorflow.python.ops import functional_ops

from tensorflow.python.ops import ctc_ops

from tensorflow.python.ops import clip_ops

from tensorflow.python.ops import gen_array_ops

