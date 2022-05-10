import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double)

def func1(x, y):
    return x**2 + y**2

f1 = FUNTYPE(func1)

def func2(x, y):
    return x**2 - y**2

f2 = FUNTYPE(func2)

def func3(x, y):
    return x**2 - y**2 - x*y

f3 = FUNTYPE(func3)

def func4(x, y):
    return x**2 + y**2 - x*y

f4 = FUNTYPE(func4)

def func5(x, y):
    return x**2 + y**2 - x*y - y**2

f5 = FUNTYPE(func5)

def func6(x, y):
    return x**2 + y**2 - x*y + y**2

f6 = FUNTYPE(func6)

def func7(x, y):
    return x**2 + y**2 - x*y
