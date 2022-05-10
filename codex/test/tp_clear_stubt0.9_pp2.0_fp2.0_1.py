import gc, weakref

class LateFin:
    __slots__ = ('ref',)
    def __del__(self):
        global func
        func = self.ref()

class Cyclic(tuple):
    __slots__ = ()
    def __del__(self):
        self[1].ref = weakref.ref(self[0])
        global latefin
        del latefin

latefin = LateFin()
func = lambda: None
cyc = tuple.__new__(Cyclic, (func, latefin))

func.__module__ = cyc
del func, cyc

gc.collect(-1)
print(latefin.ref)


################################################################################
# Make sure we don't pass interned strings to the
# structseq_new function
#
# This is an internal test of the cpython implementation
################################################################################

import gc, weakref
from sys import intern
from test.support import create_string_buffer

class Func:
    def __init__(self):
        self.weakrefs = []

    def __del__(self):
        global func, buf
        func = self.cfunc
        del self.cfunc
        del self.weakrefs
        del buf

from ctypes import pythonapi
from ctypes import py_object as PyObject
from ctypes import py_object as PyObject
from ctypes import py_object as PyObject
from ctypes import py_object as PyObject
from ctypes import py_object as PyObject
from ctypes import py_object as PyObject
from ctypes import py_object as PyObject
from ctypes import py_object as PyObject
