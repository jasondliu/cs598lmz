import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1


assert fun() == 1

class A(object):
    """docstring for A"""
    def __init__(self):
        super(A, self).__init__()

    @property
    def a(self):
        return 1

assert isinstance(A, type)
assert isinstance(A(), A)
assert type(A) == type
assert type(A()) == A

import ctypes

def fun():
    pass

assert type(fun) == type
assert type(fun) == ctypes.FunctionType
assert id(fun) != id(fun)
assert id(fun) != id(fun)

assert type(dir) == ctypes.BuiltinFunctionType
assert id(dir) == id(dir)

assert type(type) == type
assert type(type) == type
assert id(type) == id(type)

d = {}
assert type(d) == dict

# import os
# import sys
# import tempfile
# from ctypes import CDLL
# from ctypes.util import find_library
# from
