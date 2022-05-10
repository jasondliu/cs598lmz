from lzma import LZMADecompressor
LZMADecompressor()

import cPickle
import gzip
import theano
import theano.tensor as T
import numpy
import argparse
import os
import urllib
import urllib2
import csv
import itertools
import math
import pickle

import matplotlib.pyplot as plt
import matplotlib.cm as cm

import numpy as np
import pandas as pd

from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.model_selection import train_test_split

def get_data(filename, scaler, test_size):
    if not os.path.exists(filename):
        print('Downloading data...')
        url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/00462/drug_consumption.data'
        urllib.urlretrieve(url, filename)
    print('Reading data...')
    df = pd.read_csv(filename, header=0)
    df.columns = [
        'ID', 'Age', '
