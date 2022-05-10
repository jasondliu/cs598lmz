import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect("file::memory:?cache=shared")

import pyaudio

import numpy
import scipy
import scipy.io
import scipy.signal

import matplotlib
import matplotlib.pyplot

import sklearn.preprocessing

import keras
import keras.backend
import keras.models
import keras.layers
import keras.utils
import keras.preprocessing
import keras.preprocessing.image


def setup_threading():
    # https://stackoverflow.com/a/17239515
    ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(threading.get_ident()), ctypes.py_object(SystemExit))

def setup_keras():
    keras.backend.set_image_data_format("channels_last")

def setup():
    setup_threading()
    setup_keras()

