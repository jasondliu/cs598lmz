import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    pass
fun()

import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun(x):
    pass
fun(33)

import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun(x, y):
    pass
fun(33, 44)

import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun(*args):
    pass
fun(33, 44)

# py_object is a speciality of the ctypes module:

import ctypes
ctypes.CFUNCTYPE(ctypes.py_object)

# ctypes will accept a pure Python, funcptr-based callback:

from pypy.tool.pairtype import extendabletype
_testcapi = testcapi
from pypy.module._cppyy import capsule
from pypy.rlib import rdynload
from pypy.rpython.ll
