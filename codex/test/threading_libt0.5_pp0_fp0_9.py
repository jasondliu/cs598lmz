import threading
threading.stack_size(2**27)
import sys

def main():
    #print(sys.path)
    import numpy as np
    from sklearn.model_selection import train_test_split
    from sklearn.linear_model import LogisticRegression
    from sklearn.neural_network import MLPClassifier
    from sklearn.svm import SVC
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.preprocessing import StandardScaler
    from sklearn.metrics import accuracy_score
    import pandas as pd

    # Importing the dataset
    dataset = pd.read_csv('data.csv')
    X = dataset.iloc[:,:-1].values
    y = dataset.iloc[:,-1].values
    #print(X)
    #print(y)
    # Splitting the dataset into the Training set and Test set
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)

   
