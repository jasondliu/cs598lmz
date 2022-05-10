import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(1)
import matplotlib as mpl
mpl.rcParams['font.family'] = 'Tahoma'
import matplotlib.pyplot as plt
%matplotlib inline
import os
import random
import numpy as np
import pandas as pd
from IPython.display import Image, clear_output
from model import *
from utils import *
import tensorflow as tf
from tensorflow.contrib.keras import backend as K
import os
import shutil

DIR = "D:\ML\Data\\"
#if not os.path.exists(DIR):
#    os.mkdir(DIR, 0o777)
    #os.makedirs(DIR)
#Note, we have copy these data to ...\Data folder because the dataset is too large. 
#If you want to reproduce the result, please remove all the data and run ..\data\download_dataset.py
#to download them.

data = {
    'train_data': os.path.join(DIR
