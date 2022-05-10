import ctypes
ctypes.windll.user32.SetProcessDPIAware()

import matplotlib.pyplot as plt
from matplotlib.widgets import Button, Slider

from scipy.signal import butter, lfilter, freqz

from sklearn.decomposition import FastICA, PCA

import numpy as np
import pandas as pd

from os import listdir, path
import sys

# read in data
# data = np.loadtxt('data.csv', delimiter=',', skiprows=1)

# read in data from csv file
data = pd.read_csv('data.csv', header=0, sep=',')

# get the data from the csv file
data = data.values

n_samples = data.shape[0]
n_features = data.shape[1]

# get the data from the csv file
data = data.values

# get the data from the csv file
data = data.values

# get the data from the csv file
data = data.values

# get the data
