import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def myfunc(x):
    return x * 2

myfunc_c = FUNTYPE(myfunc)

print(myfunc_c(5))

# ctypes.c_int.in_dll(ctypes.CDLL(None), "errno")

# ctypes.c_int.in_dll(ctypes.CDLL("libc.so.6"), "errno")

# ctypes.c_int.in_dll(ctypes.CDLL("libc.so.6"), "errno").value

# ctypes.c_int.in_dll(ctypes.CDLL("libc.so.6"), "errno").value = 2

# ctypes.c_int.in_dll(ctypes.CDLL("libc.so.6"), "errno").value

# ctypes.c_int.in_dll(ctypes.CDLL("libc.so.6"), "errno").value = 0

# ctypes.c_int.in_dll(
