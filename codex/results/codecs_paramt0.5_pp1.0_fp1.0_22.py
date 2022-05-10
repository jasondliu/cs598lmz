import codecs
codecs.register_error('strict', codecs.ignore_errors)

import numpy as np
import pandas as pd

from sklearn.preprocessing import LabelEncoder

#
# Load the data
#
train = pd.read_csv('data/train.csv')
test = pd.read_csv('data/test.csv')

#
# Convert the data to numpy arrays
#
train = train.values
test = test.values

#
# Extract the labels
#
y_train = train[:, 0]
X_train = train[:, 1:]

#
# Convert the data to float32
#
X_train = X_train.astype(np.float32)
test = test.astype(np.float32)

#
# Normalize the data
#
X_train /= 255
test /= 255

#
# Convert the labels to int32
#
y_train = y_train.astype(np.int32)

#
# Convert the labels to one-hot encoding
#
y_train = LabelEncoder().fit
