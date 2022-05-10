import ctypes
# Test ctypes.CFUNCTYPE() argument and return types.
from array import array
import _ctypes_test

try:
    unicode
except NameError:
    unicode = str

