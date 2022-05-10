import codecs
codecs.register(lambda name: name == 'cp65001' and codecs.lookup('utf-8') or None)
import csv
import cv2
import skimage.io
import matplotlib.pyplot as plt
import numpy as np
import os
import pydicom
import random
import torch
from skimage import io
# from torch.utils.data import Dataset
# from torchvision import transforms, utils

# Ignore warnings
import warnings
warnings.filterwarnings("ignore")

plt.ion()   # interactive mode

#Reading the CSV
df = pd.read_csv('./stage_2_train_labels.csv')

# print(df.head())

#Reading the images
dir_img = './stage_2_train_images/'
dir_save = './preprocessed_stage_2_train_images/'

# print(type(df))
for i in range(len(df)):
    print(i)
    id_ = df['patientId'][i]
    img = c
