import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

fun()

#%%
from ctypes import *

class POINT(Structure):
    _fields_ = [("x", c_int),
                ("y", c_int)]

pt = POINT(1, 2)
print(pt.x, pt.y)

#%%
from ctypes import *

class POINT(Structure):
    _fields_ = [("x", c_int),
                ("y", c_int)]

pt = POINT(1, 2)
print(pt.x, pt.y)

#%%
from ctypes import *

class POINT(Structure):
    _fields_ = [("x", c_int),
                ("y", c_int)]

pt = POINT(1, 2)
print(pt.x, pt.y)

#%%
from ctypes import *

class POINT(Structure):
    _fields_ = [("x", c_int),
                ("y", c_int)]

pt = POINT(1, 2)

