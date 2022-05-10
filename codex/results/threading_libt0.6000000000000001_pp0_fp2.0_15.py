import threading
threading.stack_size(2**27)

import numpy as np
import tensorflow as tf

from tensorflow.contrib.seq2seq import BahdanauAttention, AttentionWrapper, BasicDecoder, dynamic_decode, tile_batch
from tensorflow.contrib.rnn import LSTMCell, LSTMStateTuple, GRUCell, DropoutWrapper

from tensorflow.python.layers.core import Dense
from tensorflow.python.ops.rnn_cell_impl import _zero_state_tensors

from tensorflow.contrib.rnn import MultiRNNCell

from tensorflow.python.util import nest

from data_loader import *
from helper import *
from model import *

# In[4]:

# Set params

# Training params
epochs = 1
batch_size = 128
max_enc_len = 200
max_dec_len = 50

# Model params
min_dec_steps = 2
max_dec_steps = max_dec_len
beam_width = 3
