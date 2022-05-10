import ctypes
import ctypes.util
import threading
import sqlite3
import time
import logging
import sys
import os
import signal

import numpy as np

import pycuda.driver as cuda
import pycuda.autoinit
from pycuda.compiler import SourceModule

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# load the shared library
lib = ctypes.cdll.LoadLibrary(ctypes.util.find_library('libsvm_predict_wrap'))

# define argument types and return type
lib.svm_predict_wrap.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p]
lib.svm_predict_wrap.restype = ctypes.c_double

def predict(test_file, model_file, output_file):
    return lib.svm_predict_wrap(test_file.encode('utf-8'), model_file.encode('utf-8'), output_file.encode('utf-8'))

