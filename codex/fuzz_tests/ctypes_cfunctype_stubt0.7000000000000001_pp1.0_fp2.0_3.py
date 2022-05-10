import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return obj

print(fun())
</code>

The same code can be used to pass the object to a C callback, and then call a Python method on it. 
<code>import ctypes
from ctypes import c_int, c_size_t, c_void_p, cdll, POINTER
from ctypes.util import find_library
from sys import platform
from ctypes.wintypes import *
from ctypes.wintypes import DWORD
from ctypes import cast, pythonapi

class Unbuffered(object):
   def __init__(self, stream):
       self.stream = stream
   def write(self, data):
       self.stream.write(data)
       self.stream.flush()
   def writelines(self, datas):
       self.stream.writelines(datas)
       self.stream.flush()
   def __getattr__(self, attr):
       return getattr(self.stream, attr)

import sys
sys.stdout = Unbuffered(sys.stdout)

class Win32FuncPtr
