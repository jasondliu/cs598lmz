import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def func(a, b):
    print a, b
    return a + b

f = FUNTYPE(func)
print f(2, 3)

# callback
class MyClass(object):
    def __init__(self, a):
        self.a = a

    def __call__(self, b):
        print self.a, b
        return self.a + b

f = FUNTYPE(MyClass(2))
print f(3)

# callback with args
class MyClass2(object):
    def __init__(self, a):
        self.a = a

    def __call__(self, b, c):
        print self.a, b, c
        return self.a + b + c

f = FUNTYPE(MyClass2(2), (ctypes.c_int, ctypes.c_int))
print f(3, 4)

# callback with args and kwargs
class MyClass3(object):
    def
