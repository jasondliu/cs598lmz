import codecs
codecs.register(lambda name: codecs.lookup("utf-8") if name == "cp65001" else None)
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
sys.stderr = codecs.getwriter("utf-8")(sys.stderr.detach())

import glob
import numpy as np
from PIL import Image
import pdb
import time
from sklearn import neighbors, datasets
from sklearn.cluster import MiniBatchKMeans
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn import mixture
from sklearn.metrics import accuracy_score
from sklearn.neural_network import BernoulliRBM
from sklearn.model_selection import cross_val_score


n_classes = 19

def findNearest(arr, val):
	arr = np.asarray(arr)
	idx = (np.abs(arr - val)).argmin()
	return arr[idx]

def data2vw(data
