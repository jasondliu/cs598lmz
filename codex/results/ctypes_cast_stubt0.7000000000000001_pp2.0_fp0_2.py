import ctypes
ctypes.cast(id(id), ctypes.py_object).value

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('Social_Network_Ads.csv')
x = data.iloc[:,2:4].values
y = data.iloc[:,4].values

#splitting the data
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=0)

#feature scaling
from sklearn.preprocessing import StandardScaler
std = StandardScaler()
x_train = std.fit_transform(x_train)
x_test = std.transform(x_test)

#fitting the model
from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier(crit
