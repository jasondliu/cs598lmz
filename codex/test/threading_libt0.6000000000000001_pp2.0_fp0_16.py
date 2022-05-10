import threading
threading.stack_size(2**27)
import sys
import glob
import pickle
import scipy.io
import numpy as np
import scipy.io.wavfile as wav
import matplotlib.pyplot as plt
import librosa
import librosa.display
import math
import cPickle
import h5py
import os
import tensorflow as tf
from tensorflow.contrib.rnn import LSTMCell
from tensorflow.contrib.rnn import DropoutWrapper
from tensorflow.contrib.rnn import MultiRNNCell
from tensorflow.contrib.rnn import GRUCell
from tensorflow.python.ops import rnn
from tensorflow.python.ops import rnn_cell
from tensorflow.contrib.layers import fully_connected
from tensorflow.contrib.layers import batch_norm
from tensorflow.contrib.layers import xavier_initializer
from tensorflow.contrib.layers import l2_regularizer
