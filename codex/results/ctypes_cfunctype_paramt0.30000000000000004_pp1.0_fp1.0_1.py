import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def func(x):
    print 'func called with', x
    return x

cfunc = FUNTYPE(func)

print cfunc(5)

# ---------------------------------------------------------------

class MyClass(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int),
                ('b', ctypes.c_int)]

def func2(x):
    print 'func2 called with', x
    return x

cfunc2 = FUNTYPE(func2)

print cfunc2(MyClass(1, 2))

# ---------------------------------------------------------------

class MyClass2(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int),
                ('b', ctypes.c_int)]

def func3(x):
    print 'func3 called with', x
    return x

cfunc3 = FUNTYPE(func3)

print cfunc3(MyClass2(1, 2))

# ---------------------------------------------------------------

class MyClass
