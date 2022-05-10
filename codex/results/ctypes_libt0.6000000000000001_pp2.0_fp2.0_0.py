import ctypes
ctypes.windll.user32.SetProcessDPIAware()

# import necessary packages
from keras.models import load_model
import pandas as pd
import numpy as np
import cv2
import glob
import os
import matplotlib.pyplot as plt
import pickle

# load the model
model = load_model('models/model.h5')

# load the scaler
scaler = pickle.load(open('models/scaler.pkl', 'rb'))

# load the test images
test_images = glob.glob("test_images/*.jpg")

# list to store all images
image_list = []

# loop over all images
for image in test_images:
    # open the image and resize it to (128, 128)
    img = cv2.imread(image)
    img = cv2.resize(img, (128, 128))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    # add the image to the list of images

