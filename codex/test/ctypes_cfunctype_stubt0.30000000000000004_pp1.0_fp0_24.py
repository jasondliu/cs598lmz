import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

print(fun())

# 回调函数
@FUNTYPE
def fun2(x):
    return x * 2

print(fun2(5))

# 回调函数
@FUNTYPE
def fun3(x, y):
    return x + y

print(fun3(5, 6))

# 回调函数
@FUNTYPE
def fun4(x, y, z):
    return x + y + z

print(fun4(5, 6, 7))

# 回调函数
@FUNTYPE
def fun5(x, y, z, w):
    return x + y + z + w

print(fun5(5, 6, 7, 8))

# 回调函数
@FUNTYPE
def fun6(x, y, z, w, v):
    return x + y + z + w + v

