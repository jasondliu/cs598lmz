import threading
threading.stack_size(2**27)

# Use the 'reload' method so that module code gets reloaded when changed
import sys
import importlib
importlib.reload(sys)

import tensorflow as tf
import numpy as np
import os, time
import cifar10
import cifar10_input


# Define some global variables
FLAGS = tf.app.flags.FLAGS
tf.app.flags.DEFINE_string('train_dir', '/tmp/cifar10_train',
                           """Directory where to write event logs """
                           """and checkpoint.""")
tf.app.flags.DEFINE_integer('max_steps', 1000000,
                            """Number of batches to run.""")
tf.app.flags.DEFINE_boolean('log_device_placement', False,
                            """Whether to log device placement.""")
tf.app.flags.DEFINE_integer('log_frequency', 10,
                            """How often to log results to the console.""")


def train():
    """Train CIFAR-10 for a number of
