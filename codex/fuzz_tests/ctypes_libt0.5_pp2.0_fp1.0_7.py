import ctypes
ctypes.cdll.LoadLibrary('libmkl_avx2.so')
ctypes.cdll.LoadLibrary('libmkl_def.so')
ctypes.cdll.LoadLibrary('libmkl_vml_avx2.so')
ctypes.cdll.LoadLibrary('libmkl_vml_def.so')

import sys
sys.path.append('../../')
from src.models.cnn_model import CNNModel
from src.utils.train_utils import *
from src.utils.data_utils import *

# data
print("Load Data")
train_data, train_label, test_data, test_label = load_data()

# model
model = CNNModel(train_data.shape[1:])

# train
print("Start Training")
model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=1e-4),
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

train
