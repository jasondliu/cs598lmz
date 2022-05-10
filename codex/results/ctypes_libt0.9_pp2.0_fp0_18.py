import ctypes
ctypes.windll.user32.SetProcessDPIAware()

import numpy as np
from tqdm import tqdm
import random

from keras.models import Sequential
from keras.layers import Dense, Dropout, Conv2D, MaxPool2D, Activation, Flatten
from keras.callbacks import TensorBoard


# Preprocess the data
data_preprocess = ImagePreprocess("images/")
data_preprocess.perform_preprocessing()

print("Preprocessed Training Data : ", data_preprocess.training_data)
print("Preprocessed Testing Data : ", data_preprocess.test_data)

# Reshape training and testing data
train_data_x = np.asarray([i[0] for i in data_preprocess.training_data])
train_data_y = [i[1] for i in data_preprocess.training_data]

test_data_x = np.asarray([i[0] for i in data_preprocess.test_data])
test_data_y = [i[1] for
