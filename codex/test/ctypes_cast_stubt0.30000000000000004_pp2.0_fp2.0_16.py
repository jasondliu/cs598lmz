import ctypes
ctypes.cast(0, ctypes.py_object)

#This is a workaround for a bug in the Python interpreter:
#http://bugs.python.org/issue15881#msg170215

import sys
if sys.version_info[0] == 2:
    import thread
else:
    import _thread as thread

import time

import numpy as np

