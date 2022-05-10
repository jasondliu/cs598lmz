import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def myfunc(x):
    return x*2

f = FUNTYPE(myfunc)
print(f(3))

# ctypes.c_int.in_dll(ctypes.cdll.msvcrt, "errno")

# ctypes.c_int.in_dll(ctypes.cdll.msvcrt, "errno").value = 0

# ctypes.c_int.in_dll(ctypes.cdll.msvcrt, "errno").value

# ctypes.c_int.in_dll(ctypes.cdll.msvcrt, "errno")

# ctypes.c_int.in_dll(ctypes.cdll.msvcrt, "errno").value = 0

# ctypes.c_int.in_dll(ctypes.cdll.msvcrt, "errno").value

# ctypes.c_int.in_dll(ctypes.cdll.msvcrt, "errno
