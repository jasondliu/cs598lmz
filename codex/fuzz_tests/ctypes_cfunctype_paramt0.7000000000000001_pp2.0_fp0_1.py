import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double,ctypes.c_double)
pow = FUNTYPE(ctypes.pythonapi.PyFloat_AsDouble)

def power(A,n):
    return pow(A,n)
# print(pow(2.0,3.0))
print(power(2.0,3.0))
