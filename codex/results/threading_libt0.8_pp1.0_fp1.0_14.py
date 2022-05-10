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
model = keras.models.Sequential([
  keras.layers.Conv2D(64, (3,3), padding='same', activation='relu', input_shape=(26, 26, 1)),
  keras.layers.Conv2D(64, (3,3), activation='relu'),
  keras.layers.MaxPooling2D((2,2)),
  keras.layers.Conv2D(128, (3,3), padding='same', activation='relu'),
  keras.layers.Conv2D(128, (3,3), activation='
