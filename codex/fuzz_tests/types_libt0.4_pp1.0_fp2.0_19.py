import types
types.ModuleType.__repr__ = lambda self: "<module '%s'>" % self.__name__

import os
import sys
import time
import math
import numpy as np
import cv2
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.lines as lines
from matplotlib.patches import Polygon
import IPython.display
import tensorflow as tf

from object_detection.utils import label_map_util
from object_detection.utils import visualization_utils as vis_util

import logging
logger = tf.get_logger()
logger.setLevel(logging.ERROR)

# patch tf1 into `utils.ops`
utils_ops = tf.compat.v1.get_default_graph().get_operations()
all_tensor_names = {output.name for op in utils_ops for output in op.outputs}
utils_ops.stop_gradient = tf.compat.v1.stop_gradient

if tf.__version__ < '1.
