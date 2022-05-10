import ctypes
import ctypes.util
import threading
import sqlite3
import json, os, sys, re
import time, datetime
import math
import tempfile

#----------------------------------------------------------------------------------------------------------
#----------------------------Python bindings for JPL Horizons system--------------------------------------
#----------------------------------------------------------------------------------------------------------
#

#load shared library defining ephemeris API
horizonsAPI = ctypes.cdll.LoadLibrary("pyhorizons_api.so")

#Provide API with conversion functions between C and Python types
horizonsAPI.pytimestruct_to_ctimestruct.argtypes = [ctypes.py_object]
horizonsAPI.pytimestruct_to_ctimestruct.restype = ctypes.c_void_p
horizonsAPI.pytimestructarray_to_cstring.argtypes = [ctypes.py_object]
horizonsAPI.pytimestructarray_to_cstring.restype = ctypes.c_char_p

#turn on exception throwing for c++ functions (this does not affect c functions)
ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(threading.get_ident()), c
