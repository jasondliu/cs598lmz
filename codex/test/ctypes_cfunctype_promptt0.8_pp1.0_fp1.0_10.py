import ctypes
# Test ctypes.CFUNCTYPE with a non-integer return value.
import ctypes.util

funcp = ctypes.CFUNCTYPE(ctypes.py_object)

dll = ctypes.CDLL(ctypes.util.find_library('c'))

