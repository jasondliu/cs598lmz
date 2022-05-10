import ctypes
# Test ctypes.CFUNCTYPE()
#

import sys
import ctypes
from ctypes import *

def test(typ):
    f = CFUNCTYPE(typ)
