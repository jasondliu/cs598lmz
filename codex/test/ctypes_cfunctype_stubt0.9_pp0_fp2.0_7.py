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

