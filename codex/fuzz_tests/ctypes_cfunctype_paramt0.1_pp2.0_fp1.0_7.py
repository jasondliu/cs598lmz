import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def myfunc(x):
    return x + 1

myfunc_c = FUNTYPE(myfunc)

print(myfunc_c(1))

# ctypes.c_int.in_dll(ctypes.CDLL('./libtest.so'), 'x')

# ctypes.c_int.in_dll(ctypes.CDLL('./libtest.so'), 'x').value = 5

# print(ctypes.c_int.in_dll(ctypes.CDLL('./libtest.so'), 'x').value)

# print(ctypes.c_int.in_dll(ctypes.CDLL('./libtest.so'), 'x').value)

# print(ctypes.c_int.in_dll(ctypes.CDLL('./libtest.so'), 'x').value)

# print(ctypes.c_int.in_dll(ctypes.CDLL('./libtest.so'), 'x').value)

# print
