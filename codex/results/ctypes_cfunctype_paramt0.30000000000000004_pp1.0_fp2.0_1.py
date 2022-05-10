import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def py_func(x):
    print("x:", x)
    return x

c_func = FUNTYPE(py_func)

print("c_func(1):", c_func(1))

# c_func(1): x: 1
# 1
</code>

