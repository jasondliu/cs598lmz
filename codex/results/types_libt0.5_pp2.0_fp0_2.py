import types
types.FunctionType = types.LambdaType

import logging
logger = logging.getLogger(__name__)

import re

import copy
import json
import random
import string

import numpy as np

from sklearn.utils import shuffle

from tensorflow.python.keras import backend as K
from tensorflow.python.keras.models import Model
from tensorflow.python.keras.layers import Input, Embedding, LSTM, Dense, TimeDistributed, Dropout, Bidirectional, Lambda, Activation
from tensorflow.python.keras.optimizers import Adam
from tensorflow.python.keras.callbacks import Callback

import nltk

from nltk.translate.bleu_score import sentence_bleu

from . import utils

#-----------------------------------------------------------------------------#
#                              TRAINING FUNCTIONS                             #
#-----------------------------------------------------------------------------#

def train_model(model,
                input_sequences,
                output_sequences,
                epochs,
                batch_size,
               
