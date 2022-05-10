import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def test1():
    def pyfunc(a, b):
        return a+b

    callback = FUNTYPE(pyfunc)
    print callback(1, 2)

def test2():
    def pyfunc(a, b):
        return a+b

    callback = FUNTYPE(pyfunc)
    print callback(1, 2)
    callback.restype = ctypes.c_float
    print callback(1, 2)

def test3():
    def pyfunc(a, b):
        return a+b

    callback = FUNTYPE(pyfunc)
    print callback(1, 2)
    callback.argtypes = (ctypes.c_float, ctypes.c_float)
    print callback(1, 2)

def test4():
    class MyClass(object):
        def __init__(self):
            self.x = 1
            self.y = 2
            self.z = 3
            self.s = "Hello"

        def __call
