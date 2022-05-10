import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def c_callback(a,b):
    print "c_callback",a,b
    return a+b

callback = FUNTYPE(c_callback)

class A(object):
    def __init__(self):
        self.callback = callback
        self.callback.restype = ctypes.c_int
        self.callback.argtypes = [ctypes.c_int, ctypes.c_int]
        self.count = 0

    def __call__(self, a, b):
        print "A.__call__", a, b
        self.count += 1
        return self.callback(a, b)

a = A()

#py_callback = ctypes.pythonapi.PyCFunction_NewEx(
py_callback = ctypes.pythonapi.PyCFunction_New(
    ctypes.py_object(a),
    ctypes.py_object(None),
    ctypes.py_object(a))

import sys
if
