import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def fun(x):
    return x**2

f = FUNTYPE(fun)
print(f(2))

# ctypes.c_double(2)
# ctypes.c_double(4)

# ctypes.c_double(3)
# ctypes.c_double(9)

# ctypes.c_double(4)
# ctypes.c_double(16)

# ctypes.c_double(5)
# ctypes.c_double(25)

# ctypes.c_double(6)
# ctypes.c_double(36)

# ctypes.c_double(7)
# ctypes.c_double(49)

# ctypes.c_double(8)
# ctypes.c_double(64)

# ctypes.c_double(9)
# ctypes.c_double(81)

# ctypes.c_double(10)
# ctypes.c_double(100)

# ctypes
