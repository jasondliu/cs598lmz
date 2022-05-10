import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)
import sys
sys.path.append('/usr/local/lib/python2.7/dist-packages/')
import cv2
import os
import glob
import sklearn
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cross_validation import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix
import itertools
np.set_printoptions(threshold=np.nan)

label = []
data = []
label_test = []
data_test = []

os.chdir('/home/pranay/Downloads/MNIST/MNIST')
print
