import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return [1, 2]

def f():
    g()

def g():
    fun()

f()

for i in range(1000):
    try:
        f()
    except:
        pass

def f():
    return [0]

for i in range(1000):
    try:
        f()
    except:
        pass

def f():
    return [0]

import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return [1, 2]

def f():
    g()

def g():
    fun()

f()

for i in range(1000):
    try:
        f()
    except:
        pass

def f():
    return [0]

for i in range(1000):
    try:
        f()
    except:
        pass

def f():
    return [0]

import ctypes
