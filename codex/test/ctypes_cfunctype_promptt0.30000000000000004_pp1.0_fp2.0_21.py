import ctypes
# Test ctypes.CFUNCTYPE

# This is a test of ctypes.CFUNCTYPE.  It should print:
#
#   1 2 3 4
#   1 2 3 4
#   1 2 3 4
#   1 2 3 4
#   1 2 3 4
#   1 2 3 4
#   1 2 3 4
#   1 2 3 4
#   1 2 3 4
#   1 2 3 4
#
# and then exit.

import sys
import ctypes
from ctypes import *

# This is the function we'll call from Python.
