from bz2 import BZ2Decompressor
BZ2Decompressor()

import csv
import cv2
import numpy as np
import json

import os
import shutil

from os import listdir
from os.path import isfile, join
import glob
import requests 
import time
import sys
import PIL.Image
import PIL.ExifTags
from PIL import Image


# In[2]:


# Global variables
Global_Image_Data = "E:/MSc Project/Python Code/Data/Automobile_Images/"
Global_Labels_Data = "E:/MSc Project/Python Code/Data/Automobile_Labels/"
PATH = "E:/MSc Project/Python Code/Data/"
IMAGE_SIZE = 120
IMAGE_WIDTH, IMAGE_HEIGHT = IMAGE_SIZE, IMAGE_SIZE
EPOCHS = 15
BATCH_SIZE = 128
TEST_SIZE = 30
CLASSES = 4

# 0: Class 0 - No Damage
# 1: Class 1 - Minor Damage
# 2: Class 2 - Moderate Damage
# 3: Class 3 - Significant Damage

# Choose/Create dataset to
