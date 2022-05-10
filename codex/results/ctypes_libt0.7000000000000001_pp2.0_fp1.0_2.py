import ctypes
ctypes.cdll.LoadLibrary('libX11.so')
ctypes.cdll.LoadLibrary('libXext.so')

import matplotlib.pyplot as plt
import numpy as np
import time
from PIL import Image

from scipy import misc
from keras.models import model_from_json
from keras.preprocessing import image
from keras.applications.resnet50 import preprocess_input
from skimage.transform import resize
from skimage.feature import hog
from skimage import exposure

from sklearn import svm
from sklearn.metrics import classification_report,accuracy_score
from sklearn.model_selection import train_test_split



# In[2]:


import cv2
from matplotlib import pyplot as plt
from IPython.display import clear_output
import os
from tqdm import tqdm
import pickle


# In[3]:


cap = cv2.VideoCapture(0)


# In[4]:


def get_img(cap):
    ret,frame = cap
