import ctypes
# Test ctypes.CFUNCTYPE() with reordered arguments and calling convention.
from ctypes import *
myfun = CFUNCTYPE(c_int, c_char_p, c_int)(lambda s, x: len(s) + x)
myfun(b"hello", 4)

# http://bugs.python.org/issue29682
# issue29682: Regression in Issue#30117 causes Tkinter to fail to load
# during interpreter shutdown
from tkinter import Tk
tk = Tk()
tk.destroy()
del tk

# heap copy of interned string tuples on Python 3
# https://github.com/python/cpython/pull/14414
import struct, sys, os.path
path = os.path.dirname(__file__) + os.sep + "big-tuple.bin"
with open(path, "rb") as f:
    data = f.read()

s = struct.unpack("{}L".format(len(data)//8), data)
tuple(s)

import protocolbuffers
proto = protocolbuffers
