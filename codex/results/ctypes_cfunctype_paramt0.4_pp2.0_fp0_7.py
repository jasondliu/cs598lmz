import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def add(a, b):
    return a + b

add_func = FUNTYPE(add)

print add_func(1, 2)

# 可以在Python里面调用C代码，也可以在C代码里面调用Python代码。
# 在Python里面调用C代码，可以通过ctypes模块，或者Cython。
# 在C代码里面调用Python代码，可以通过SWIG，或者Cython。

# 在C代码里面调用Python代码，实际上是调用Python的
