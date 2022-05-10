import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()

import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import time
import math
import numpy as np
import scipy.io as sio

from matplotlib import pyplot as plt

from utils.general import *
from utils.plotter import *
from utils.data_manipulation import *
from utils.data_io import *
from utils.signal_processing import *

from utils.evaluation import *

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
from sklearn.metrics.pairwise import pairwise_distances

from sklearn.mixture import GaussianMixture

from scipy.cluster.hierarchy import dendrogram, linkage

from sklearn.decomposition import PCA
