import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'cp65001' else None)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
dataset = pd.read_csv("H:/Predictive Analysis/Machine Learning/OSR/project/Python-lessons/Naive Bayes/Social_Network_Ads.csv")
X = dataset.iloc[:, [2, 3]].values
y = dataset.iloc[:, 4].values
# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)
# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)
# Fitting Naive Bayes to the Training
