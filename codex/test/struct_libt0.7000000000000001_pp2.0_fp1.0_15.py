import _struct

import cv2
import numpy as np
import matplotlib.pyplot as plt

from sklearn import preprocessing
from sklearn.cluster import KMeans

from scipy.cluster.vq import vq, kmeans

from scipy.spatial.distance import euclidean

plt.rcParams['figure.figsize'] = (16.0, 8.0)

def get_frame_index(frame_index):
	if frame_index > 9:
		return str(frame_index)
	else:
		return '0' + str(frame_index)

def get_frame(name):
	image = cv2.imread(name)
	return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

def get_semantic_frame(frames, frame_index, frame_count):
	frame = frame_index - frame_count
	if frame < 0:
		frame = 0

	return frames[frame_index]
	
