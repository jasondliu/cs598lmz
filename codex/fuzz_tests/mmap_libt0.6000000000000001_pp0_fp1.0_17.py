import mmap
import numpy as np

# This is a little bit of magic to make matplotlib figures appear inline in the
# notebook rather than in a new window.
%matplotlib inline
import matplotlib.pyplot as plt
plt.style.use('ggplot')

import os

# The data directory contains .mat files with each a dictionary
# We'll load these dictionaries into a list
DATA_DIR = './data'
data_filenames = [os.path.join(DATA_DIR, filename)
                  for filename in os.listdir(DATA_DIR)]

# Here's a function that will help us load the data from a file
def load_single_subject_data(filename):
    '''
    Loads data from a single subject.

    Returns the stimulus code for each trial, the brain data, and the
    stimulus class.
    '''
    return loadmat(filename)

# Load data from all subjects into a list
datasets = [load_single_subject_data(filename) for filename in data_filenames]

# Concatenate
