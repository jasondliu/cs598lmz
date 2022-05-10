import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'cp65001' else None)

import os
import sys
import re
import time
import shutil
import pickle
import unicodedata
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from keras.callbacks import EarlyStopping
from keras.preprocessing import image
from keras.preprocessing.sequence import pad_sequences
from keras.preprocessing.text import Tokenizer
from keras.utils import to_categorical
from keras.models import Model, model_from_json
from keras.layers import Input, Dense, Dropout, Activation, LeakyReLU, InputSpec, Concatenate
from keras.layers import TimeDistributed, Conv2D, MaxPooling2D, Reshape, Lambda, Bidirectional, Flatten, LSTM, GRU, CuDNNLSTM
from keras.layers.merge import add, concatenate
from keras.layers.normalization import B
