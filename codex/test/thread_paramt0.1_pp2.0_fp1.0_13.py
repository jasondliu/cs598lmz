import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()

import os
import time
import numpy as np
import tensorflow as tf
import tensorflow.contrib.slim as slim
import scipy.misc
import scipy.io
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.gridspec as gridspec
from tensorflow.examples.tutorials.mnist import input_data

from ops import *
from utils import *

