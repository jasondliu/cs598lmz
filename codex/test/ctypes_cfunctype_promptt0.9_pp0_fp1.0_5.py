import ctypes
# Test ctypes.CFUNCTYPE(), and if it can be called in two ways:
#
#     CFUNCTYPE(restype, *argtypes)(callable)
#     CFUNCTYPE(restype, *argtypes)(address, [optional_flags])

import unittest
