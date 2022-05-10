import codecs
codecs.register_error("replace_with_space", lambda e: (u" ", e.start + 1))
import re
import os
import collections
import numpy as np
import pickle
import tensorflow as tf


###### This script generates simplified models and generates data for the models ######
data_path = "data"


################# Simplified model #################
def write_simplified_model(filename, vocab_size):
    """
    Generate a simplified model and write to file.
    """
    f = codecs.open(filename, "w", "utf-8")
    f.write("n-grams for word prediction: 1\n")
    # f.write("hidden_size: " + str(hidden_size) + "\n")
    # f.write("hidden_layer_size: " + str(hidden_layer_size) + "\n")
    # f.write("min_count: " + str(min_count) + "\n")
    f.write("vocab_size: " + str(vocab_size) + "\n")
    f.write("skip
