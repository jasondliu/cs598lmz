import ctypes
# Test ctypes.CFUNCTYPE

# This is a test of ctypes.CFUNCTYPE.  It is a bit more complex than the
# other tests, because it uses a function pointer as a parameter to a
# function.

import unittest
from ctypes import *

