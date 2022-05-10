import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    def f():
        return 1
    return f

def test_fun():
    assert fun()() == 1
    
from ctypes import c_int, c_float

@FUNTYPE
def fun2(a, b):
    def f():
        return a + b
    return f

def test_fun2():
    assert fun2(c_int(1), c_float(2))() == 3.0
