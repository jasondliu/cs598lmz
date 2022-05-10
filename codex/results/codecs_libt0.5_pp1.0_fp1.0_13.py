import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

import os
import sys
import time

import numpy as np
import pandas as pd

import tensorflow as tf
from sklearn.metrics import roc_auc_score

from data_loader import build_features, gen_batches, gen_test_batches
from model import TextCNN

# Parameters
# ==================================================

# Data loading params
tf.flags.DEFINE_float("dev_sample_percentage", .1, "Percentage of the training data to use for validation")
tf.flags.DEFINE_string("training_data_file", "../data/train.csv", "Data source for the training data.")
tf.flags.DEFINE_string("test_data_file", "../data/test.csv", "Data source for the test data.")

# Model Hyperparameters
tf.flags.DEFINE_integer("embedding_dim", 128, "Dimensionality of character embedding (default: 128)")
tf.flags.
