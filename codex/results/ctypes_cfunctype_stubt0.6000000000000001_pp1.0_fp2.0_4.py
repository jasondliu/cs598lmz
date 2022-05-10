import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 'hi'

fun()

def fun2():
    pass

FUNTYPE2 = ctypes.CFUNCTYPE(None)

@FUNTYPE2
def fun3():
    pass

def fun4(x):
    return x

FUNTYPE3 = ctypes.CFUNCTYPE(ctypes.py_object, ctypes.py_object)

@FUNTYPE3
def fun5(x):
    return x

def fun6(x, y):
    return x, y

FUNTYPE4 = ctypes.CFUNCTYPE(ctypes.py_object, ctypes.py_object, ctypes.py_object)

@FUNTYPE4
def fun7(x, y):
    return x, y

def fun8(x, y, z):
    return x, y, z

FUNTYPE5 = ctypes.CFUNCTYPE(ctypes.py_object, ctypes.py_object, ctypes.py_object, ctypes.py_object)

@FUNTYPE5
def fun9(x
