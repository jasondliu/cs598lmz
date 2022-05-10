import types
types.ModuleType.__call__ = lambda self, *args, **kwargs: self

from tensorflow.python.platform import flags
flags.DEFINE_string('f', '', 'kernel')

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from tensorflow.python.client import timeline
from tensorflow.python.profiler import model_analyzer
from tensorflow.python.profiler import option_builder

import models
import tools
import data_loader

