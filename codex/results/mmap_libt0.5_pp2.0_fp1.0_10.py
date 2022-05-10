import mmap
import os
import sys
import time
from datetime import datetime
from random import randint
from threading import Thread
from time import sleep

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

from utils import *

# global variables
# global variables
classifier = None
scaler = None

# the function to train the classifier
def train_classifier(train_data, train_labels):
    global classifier
    global scaler
    # machine learning code
    # prepare the data
    # split the data into train and test
    X_train, X_test, y_train, y_test = train_test_split(train_data, train_labels, test_size = 0.3, random_state = 0)
    # scale the data
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    X_test = sc.transform(X_
