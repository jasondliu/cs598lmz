import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def func(x):
    return x**2

f = FUNTYPE(func)
print(f(2))

def func2(x):
    return x**3

f2 = FUNTYPE(func2)
print(f2(2))

def func3(x):
    return x**4

f3 = FUNTYPE(func3)
print(f3(2))

def func4(x):
    return x**5

f4 = FUNTYPE(func4)
print(f4(2))

def func5(x):
    return x**6

f5 = FUNTYPE(func5)
print(f5(2))

def func6(x):
    return x**7

f6 = FUNTYPE(func6)
print(f6(2))

def func7(x):
    return x**8

f7 = FUNTYPE(func7)
print(f7(2))

def func8(x):
    return x**9
