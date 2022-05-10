import mmap
import numpy as np
import os
import re
import sys

from keras.models import Model
from keras.layers import Input, Dense, Dropout
from keras.layers import Embedding
from keras.layers import LSTM, Bidirectional
from keras.layers import Conv1D, MaxPooling1D
from keras.layers import Flatten
from keras.layers import Concatenate

from keras.utils import to_categorical
from keras.preprocessing.sequence import pad_sequences

