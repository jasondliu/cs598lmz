import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def callback(a, b):
    return a + b

cfunc = FUNTYPE(callback)

print(cfunc(2, 3))

# 可以通过ctypes.CFUNCTYPE创建一个函数类型对象，然后通过函数类型对象的实例化来创建一个回调函数。
# 回调函数的参数类型必须和函数类型对象的参数类型完全一致。

# 回调函数的参数类型必须和函
