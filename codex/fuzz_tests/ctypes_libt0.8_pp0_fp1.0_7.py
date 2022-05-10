import ctypes
ctypes.cdll.LoadLibrary('liblbfgs.dylib')
# import theano
#
# theano.config.floatX = 'float64'
# theano.config.device = 'gpu'
# import sys
# import numpy as np
# sys.path.append('../')
#
# from keras.models import Sequential
# from keras.layers.core import Dense, Dropout, Activation, TimeDistributedDense, \
#     Merge
# from keras.layers.recurrent import LSTM
# from keras.utils import np_utils
#
# from ReadData import *
# from LSTM_TIMIT_Feat_V1 import *
# from Settings import *
# from Plot_History import *
#
# # Set training params
# # -------------------
#
# # Data Path
# path_to_data = '../../Data/'
# # Train params
# BATCH_SIZE = 100
# NB_EPOCHS = 100
# # Save model
# save_model = True
# path_to_save_model
