import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def func(a, b):
    return a + b

cfunc = FUNTYPE(func)

print(cfunc(1, 2))

# ctypes.c_int.in_dll(ctypes.CDLL("./libtest.so"), "a").value
# ctypes.c_int.in_dll(ctypes.CDLL("./libtest.so"), "b").value

# ctypes.c_int.in_dll(ctypes.CDLL("./libtest.so"), "a").value = 3
# ctypes.c_int.in_dll(ctypes.CDLL("./libtest.so"), "b").value = 4
#
# ctypes.c_int.in_dll(ctypes.CDLL("./libtest.so"), "a").value
# ctypes.c_int.in_dll(ctypes.CDLL("./libtest.so"), "b").value

# ctypes.CDLL(".
