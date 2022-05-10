import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()

import os
import time
import numpy as np
import tensorflow as tf
import tensorflow.contrib.slim as slim
from tensorflow.python.ops import control_flow_ops
from tensorflow.python.ops import data_flow_ops
from tensorflow.python.ops import variables
from tensorflow.python.ops import state_ops
from tensorflow.python.framework import ops
from tensorflow.python.training import queue_runner
from tensorflow.python.ops import array_ops
from tensorflow.python.ops import math_ops
from tensorflow.python.ops import nn_ops
from tensorflow.python.ops import init_ops
from tensorflow.python.ops import variable_scope
from tensorflow.python.ops import logging_ops
from tensorflow.python.ops import gen_array_ops
from tensorflow.python.ops import random_ops
from tensorflow.python.ops import linalg_ops
