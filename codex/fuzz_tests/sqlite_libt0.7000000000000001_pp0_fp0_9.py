import ctypes
import ctypes.util
import threading
import sqlite3
import hashlib

import numpy as np

from scipy.stats import mode

from vlfeat import sift

import pygtk
pygtk.require('2.0')
import gtk
import gtk.gdk as gdk

# ------------------------------------------------------------------------------

_sift_lib = ctypes.cdll.LoadLibrary(ctypes.util.find_library('vl'))

_sift_lib.vl_sift_new.restype = ctypes.c_void_p
_sift_lib.vl_sift_new.argtypes = [ctypes.c_int, ctypes.c_int]
_sift_lib.vl_sift_delete.restype = None
_sift_lib.vl_sift_delete.argtypes = [ctypes.c_void_p]
_sift_lib.vl_sift_process_first_octave.restype = ctypes.c_int
_sift_lib.vl_sift_process_first_octave.argtypes = [ctypes.c_void
