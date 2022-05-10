import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

import sys
import os
import cv2
import glob
import csv
import numpy as np
from scipy.spatial import distance
from scipy.spatial.distance import cdist
from scipy.stats import multivariate_normal
from matplotlib import pyplot as plt
from sklearn.mixture import GaussianMixture
from sklearn.metrics import silhouette_score
from sklearn.cluster import KMeans

def load_data(path):
	data = []
	for infile in glob.glob( os.path.join(path, '*.*') ):
		img = cv2.imread(infile)
		img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
		img_rgb = img[:,:,::-1]
		data.append(img_rgb)
	return np.array(data)


def get_dominant
