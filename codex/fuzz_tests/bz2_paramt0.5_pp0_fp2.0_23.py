from bz2 import BZ2Decompressor
BZ2Decompressor

import numpy as np
import tensorflow as tf

from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder

import matplotlib.pyplot as plt
%matplotlib inline

import os
import sys
import tarfile
import random
import pickle

from six.moves import urllib

import pandas as pd


def download_file(url, destination_path, file_name):
    if not os.path.exists(destination_path):
        os.makedirs(destination_path)
    file_path = os.path.join(destination_path, file_name)
    if not os.path.exists(file_path):
        file_path, _ = urllib.request.urlretrieve(url + file_name, file_path)
        statinfo = os.stat(file_path)
        print('Successfully downloaded', file_name, statinfo.st_size, 'bytes.')
    else:
        print('File', file_name, 'already
