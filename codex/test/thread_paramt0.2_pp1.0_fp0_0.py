import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn

# Importing the dataset
dataset = pd.read_csv('creditcard.csv')

# Exploring the dataset
print(dataset.columns)
print(dataset.shape)
print(dataset.describe())

# Taking a sample of the dataset
data = dataset.sample(frac = 0.1, random_state = 1)

# Plotting histogram of each parameter
data.hist(figsize = (20, 20))
plt.show()

# Determining number of fraud cases in dataset
Fraud = data[data['Class'] == 1]
Valid = data[data['Class'] == 0]

outlier_fraction = len(Fraud) / float(len(Valid))
print(outlier_fraction)

print('Fraud Cases: {}'.format(len(Fraud)))
