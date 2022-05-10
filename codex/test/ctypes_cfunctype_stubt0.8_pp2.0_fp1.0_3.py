import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 'hi'

from ctypes import *
from ctypes.util import find_library
import os
from os.path import join, abspath, dirname
from sys import platform as _platform
