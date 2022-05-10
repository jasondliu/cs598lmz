import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()

import numpy as np
import tensorflow as tf
import time
import os

from tensorflow.python.client import timeline

from google.protobuf import text_format
from tensorflow.core.framework import graph_pb2
from tensorflow.python.client import timeline

# from tensorflow.python.profiler import option_builder
# from tensorflow.python.profiler import model_analyzer

from tensorflow.python.platform import gfile

def get_graph_def_from_file(graph_filepath):
  tf.reset_default_graph()
  with tf.Session() as sess:
    with gfile.FastGFile(graph_filepath,'rb') as f:
      graph_def = tf.GraphDef()
      graph_def.ParseFromString(f.read())
      return graph_def

