import threading
threading.stack_size(2 ** 27)

# Suppress warnings about CPU.
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# Other imports.
import numpy as np
import tensorflow as tf
from tensorflow import keras

# Constants.
NUM_CLASSES = 2
CHARS = list("abcdefghijklmnopqrstuvwxyz ")

# Classifier.
