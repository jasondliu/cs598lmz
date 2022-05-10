import sys, threading
threading.Thread(target=lambda: sys.stdout.write("\n")).start()

# Import the necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Import the necessary sklearn libraries
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

# Import the dataset
dataset = pd.read_csv('Social_Network_Ads.csv')

# Split the dataset into independent and dependent variables
X = dataset.iloc[:, [2, 3]].values
Y = dataset.iloc[:, 4].values

# Split the dataset into training and
