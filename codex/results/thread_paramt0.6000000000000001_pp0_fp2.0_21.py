import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()

import os
import sys
import json
import tensorflow as tf
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense, Embedding, Input, LSTM, GRU, Bidirectional, TimeDistributed, Dropout
from tensorflow.keras.layers import Activation, RepeatVector, Permute, Lambda, Multiply, Concatenate
from tensorflow.keras.layers import Dot, Softmax, Add
from tensorflow.keras.callbacks import ModelCheckpoint
from tensorflow.keras.callbacks import Callback
from tensorflow.keras.optimizers import Adam
from tensorflow.keras import backend as K
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import load_model
import numpy as np
import matplotlib.pyplot as plt
import math
from sklearn.model_selection import
