import threading
threading.stack_size(2**27)
import sys
import tensorflow as tf
sys.path.append("../../")
sys.path.append("../")
sys.path.append("./")
import time
import pickle
import math
import gym
import numpy as np
import utils
from tensorflow.python.ops import math_ops
from tensorflow.python.ops import nn
from tensorflow.python.ops import nn_ops
from tensorflow.python.ops import array_ops
import os
import random
import argparse
from policy_net import Policy_net
#from value_net import Value_net
from worker import Worker
from env import create_env
import multiprocessing
import shutil
import scipy.misc
import matplotlib.pyplot as plt
from skimage.measure import block_reduce

os.environ["CUDA_VISIBLE_DEVICES"] = "0"

seed = 10
random.seed(seed)
np.random.seed(seed)
tf.set_random_seed(seed
