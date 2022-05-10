import ctypes
# Test ctypes.CFUNCTYPE and a subclass of ctypes.Structure.
# It checks that the callee receives the correct type of argument.
# Test needs -fPIC on linux.

from ctypes import *
