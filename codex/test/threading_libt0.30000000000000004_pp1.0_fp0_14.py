import threading
threading.stack_size(2**27)
import sys
import glob
import pickle
sys.path.append('../../../../venv/Lib/site-packages')

from keras.models import Sequential, load_model
from keras.layers import Dense, Dropout, Conv2D, MaxPooling2D, Activation, Flatten, BatchNormalization
from keras.callbacks import TensorBoard
from collections import deque
import time
import random
from tqdm import tqdm
import os
from PIL import Image
import numpy as np
import cv2
import matplotlib.pyplot as plt
from keras.utils import to_categorical

REPLAY_MEMORY_SIZE = 50000  # How many last steps to keep for model training
MIN_REPLAY_MEMORY_SIZE = 1000  # Minimum number of steps in a memory to start training
MINIBATCH_SIZE = 64  # How many steps (samples) to use for training
