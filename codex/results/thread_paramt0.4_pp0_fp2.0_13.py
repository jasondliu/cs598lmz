import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H'),daemon=True).start()

# Imports
import numpy as np
import matplotlib.pyplot as plt
import cv2
import os
import time
import math
import random
import scipy.io
import skimage.io
import skimage.transform
import skimage.color
import skimage
import urllib.request
import shutil
import pickle
import tensorflow as tf

from PIL import Image
from skimage import io
from skimage import transform
from skimage import color
from skimage import exposure
from skimage import feature
from sklearn.svm import LinearSVC
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.datasets import make_classification
from sk
