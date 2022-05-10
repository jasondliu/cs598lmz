import ctypes
# Test ctypes.CFUNCTYPE, keyword args
from ctypes import *

try:
    WINFUNCTYPE
except NameError:
    WINFUNCTYPE = CFUNCTYPE

