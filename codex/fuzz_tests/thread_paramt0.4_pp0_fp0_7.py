import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()

import numpy as np
from scipy.spatial import distance

from sklearn.cluster import KMeans
from sklearn.manifold import TSNE
from sklearn.decomposition import PCA

from sklearn.preprocessing import normalize

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.colors as mcolors

from tqdm import tqdm

import os
import gc

import warnings
warnings.filterwarnings('ignore')

#import seaborn as sns
#sns.set()

from IPython.display import clear_output

import tensorflow as tf

from tensorflow.keras.models import Sequential, Model
from tensorflow.keras.layers import Dense, Dropout, Flatten, Input, BatchNormalization, Activation
from tensorflow.keras.layers import Conv2D, MaxPooling2D, GlobalAveragePooling2D, Global
