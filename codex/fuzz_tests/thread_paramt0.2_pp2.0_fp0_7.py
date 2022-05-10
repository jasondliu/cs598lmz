import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()

import os
import time
import random
import numpy as np
import tensorflow as tf
import tensorflow.contrib.slim as slim
import scipy.signal
from helper import *
from vizdoom import *
from random import choice
from time import sleep
from time import time

# Copies one set of variables to another.
# Used to set worker network parameters to those of global network.
def update_target_graph(from_scope,to_scope):
    from_vars = tf.get_collection(tf.GraphKeys.TRAINABLE_VARIABLES, from_scope)
    to_vars = tf.get_collection(tf.GraphKeys.TRAINABLE_VARIABLES, to_scope)

    op_holder = []
    for from_var,to_var in zip(from_vars,to_vars):
        op_holder.append(to_var.assign(from_var))
    return op_holder

# Discounting function used to
