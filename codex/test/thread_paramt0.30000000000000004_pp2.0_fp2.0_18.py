import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()

import os
import time
import math
import numpy as np
import tensorflow as tf
import tensorflow.contrib.slim as slim
import scipy.misc
import scipy.io
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.gridspec as gridspec
import cv2
import csv
import random
import pickle
from PIL import Image
from tensorflow.python.framework import ops
from tensorflow.python.ops import gen_nn_ops
from tensorflow.python.ops import array_ops
from tensorflow.python.ops import math_ops
from tensorflow.python.ops import nn_ops
from tensorflow.python.ops import control_flow_ops
from tensorflow.python.ops import linalg_ops
from tensorflow.python.ops import clip_ops
from tensorflow.python.ops import embedding_ops
from tensorflow.python.ops import rnn
