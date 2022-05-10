import mmap
import multiprocessing
import pickle
import psutil
import random
import re
import subprocess
import sys

sys.path.append('%s/tensorflow/tensorflow/models/' % os.environ['BRO ot'])
sys.path.append('%s/tensorflow/tensorflow/python/lib/' % os.environ['BRO ot'])

import cifar10_input

FLAGS = tf.app.flags.FLAGS
tf.app.flags.DEFINE_string('train_dir', '%s/data/cifar10' % os.environ['BRO ot'],
                           """Directory where to write event logs """
                           """and checkpoint.""")

tf.app.flags.DEFINE_integer('max_steps', 20000,
                            """Number of batches to run.""")

tf.app.flags.DEFINE_boolean('log_device_placement', False,
                            """Whether to log device placement.""")

