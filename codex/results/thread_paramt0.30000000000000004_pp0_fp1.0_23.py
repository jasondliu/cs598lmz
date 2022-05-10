import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score

from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam

%matplotlib inline

np.random.seed(0)

print('Modules are imported.')

# import data
data = pd.read_csv('../input/iris.csv')
data.head()

# data info
data.info()

# data description
data.describe()

# data visualization
data.hist(edgecolor='black', linewidth=1.2)
plt.show()

# data visualization
plt.figure(figsize=(12,10))
plt.subplot(2,2,1
