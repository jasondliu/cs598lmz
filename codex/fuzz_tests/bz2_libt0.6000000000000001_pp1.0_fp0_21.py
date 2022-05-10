import bz2
bz2.BZ2File
import numpy as np
import pickle as pkl
import os
import sys

# Path to the data txt file on disk.
data_path = './data/wikitext-103/'

# Check if the data path exists
if not os.path.exists(data_path):
    raise Exception("The data path "+data_path+" doesn't exist. Please download the dataset using the code provided on the website.")

# Load the vocabulary
with open(data_path + 'wiki.vocab.pkl', 'rb') as f:
    word_to_id, id_to_word, _ = pkl.load(f)
vocab_size = len(word_to_id)

# Load the test and dev data
test_data = bz2.BZ2File(data_path + 'wiki.test.bz2', 'r')
dev_data = bz2.BZ2File(data_path + 'wiki.dev.bz2', 'r')

def read_data(f):
    data = []
