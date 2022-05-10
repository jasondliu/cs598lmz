import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

'''
def f(x):
    return x**2

f = FUNTYPE(f)
print(f(2))
'''

f = FUNTYPE(lambda x: x**2)
print(f(2))
