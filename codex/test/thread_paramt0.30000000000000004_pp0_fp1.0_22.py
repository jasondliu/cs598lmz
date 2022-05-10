import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()

import sys
import os
import time
import numpy as np
import tensorflow as tf
from tensorflow.python.client import timeline
from tensorflow.python.client import device_lib

from tensorflow.python.ops import control_flow_ops
from tensorflow.python.ops import math_ops
from tensorflow.python.ops import state_ops
from tensorflow.python.framework import ops
from tensorflow.python.training import optimizer

import horovod.tensorflow as hvd

# Horovod: initialize Horovod.
hvd.init()

# Horovod: pin GPU to be used to process local rank (one GPU per process)
config = tf.ConfigProto()
config.gpu_options.allow_growth = True
config.gpu_options.visible_device_list = str(hvd.local_rank())

# Horovod: adjust number of steps based on number of GPUs.
num_steps = 100

# Horovod: adjust learning rate based
