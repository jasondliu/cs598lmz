import ctypes
# Test ctypes.CFUNCTYPE() with reordered arguments and calling convention.
from ctypes import *
myfun = CFUNCTYPE(c_int, c_char_p, c_int)(lambda s, x: len(s) + x)
myfun(b"hello", 4)

# http://bugs.python.org/issue29682
# issue29682: Regression in Issue#30117 causes Tkinter to fail to load
# during interpreter shutdown
