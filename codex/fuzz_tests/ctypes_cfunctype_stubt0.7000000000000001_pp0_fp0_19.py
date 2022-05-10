import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    print("fun called")
    return 42

fun()

fun2 = FUNTYPE(fun)
fun2()

@FUNTYPE
def fun_err():
    print("error function")
    raise RuntimeError("you should never see this")

fun_err()

import sys
sys.getrefcount(1)

sys.setdlopenflags(ctypes.RTLD_GLOBAL|ctypes.RTLD_NOW)

#%%
from ctypes import cdll

libc = cdll.LoadLibrary('libc.so.6')
libc.printf(b"Hello, %s!\n", b"world")

libm = cdll.LoadLibrary('libm.so.6')
libm.cos(3.14159 / 4)

from ctypes import *

class Point(Structure):
    _fields_ = [('x', c_int), ('y', c_int)]

Point(1, 2)
#%%
import ctypes
lib = ctypes.cdll.LoadLibrary('./mylib.so')

