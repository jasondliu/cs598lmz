import ctypes

class S(ctypes.Structure):
    x = ctypes.c_void_p.in_dll(ctypes.pythonapi, 'PyExc_ValueError')

s = S()
print(s.x)

import os
import ctypes
from ctypes import wintypes

