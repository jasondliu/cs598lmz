import socket
import sys
import time
import json
import os
import pickle
import random
import collections
import threading
from threading import Thread
import csv
import requests
from time import sleep
import datetime
import numpy as np
from numpy import array
import matplotlib.pyplot as plt
from scipy.stats import norm
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Dropout
from keras.layers import *
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from keras.callbacks import EarlyStopping
from keras.optimizers import Adam
from keras.models import load_model
import tensorflow as tf
from keras.backend.tensorflow_backend import set_session
import keras.backend as K

sess = tf.Session()
K.set_session(sess)

os.
