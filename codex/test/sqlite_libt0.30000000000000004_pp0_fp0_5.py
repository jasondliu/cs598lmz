import ctypes
import ctypes.util
import threading
import sqlite3
import time

import numpy as np
import numpy.ctypeslib as npct
import scipy.io.wavfile

import pyaudio
import wave

# load the shared object file
lib = npct.load_library("libsndfile", ".")

# setup the return types and argument types
lib.sndfile_open.restype = ctypes.c_void_p
lib.sndfile_open.argtypes = [ctypes.c_char_p, ctypes.c_int, ctypes.c_int]
lib.sndfile_close.restype = ctypes.c_int
lib.sndfile_close.argtypes = [ctypes.c_void_p]
lib.sndfile_read_int.restype = ctypes.c_int
lib.sndfile_read_int.argtypes = [ctypes.c_void_p, npct.ndpointer(dtype=np.int32, ndim=1, flags='C_CONTIGUOUS'), ctypes.c_int]
lib.sndfile
