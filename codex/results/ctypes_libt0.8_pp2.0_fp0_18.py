import ctypes
ctypes.windll.user32.SetProcessDPIAware()

from pygame import mixer
mixer.init()
mixer.music.load('/home/admin1/Music/music.mp3')
mixer.music.play()


# 1. Importing necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 2. Importing the dataset
dataset = pd.read_csv('/home/admin1/Data files/Wine_Quality_Data.csv')


# 3. Creating features and labels
features = dataset.iloc[:,:-1].values
labels = dataset.iloc[:,-1].values


# 4. Splitting the dataset into training and testing sets
from sklearn.model_selection import train_test_split
features_train,features_test,labels_train,labels_test = train_test_split(features,labels,test_size=0.20,random_state=0)


# 5. Training the Logistic Regression Model on the training set
from sklearn.
