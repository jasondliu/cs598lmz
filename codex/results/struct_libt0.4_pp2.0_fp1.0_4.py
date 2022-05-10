import _struct
import numpy as np
import time
import os
import sys
import glob
import shutil
import subprocess
import random
import string
import pdb

from scipy.io import loadmat
from scipy.io import savemat
from scipy.io import wavfile
from scipy.signal import butter, lfilter
from scipy.signal import freqz
from scipy.signal import filtfilt
from scipy.signal import resample

import matplotlib.pyplot as plt

import multiprocessing
from multiprocessing import Pool
from multiprocessing import Process
from multiprocessing import Queue
from multiprocessing import Value

from sklearn.preprocessing import normalize
from sklearn.preprocessing import scale
from sklearn.decomposition import PCA
from sklearn.decomposition import FastICA
from sklearn.decomposition import NMF

from sklearn.cluster import KMeans
from sklearn.cluster import DBSCAN

from sklearn.mixture import Gaussian
