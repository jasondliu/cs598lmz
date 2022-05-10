import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
def function(arg1, arg2):
    print(arg1, arg2)
    return arg1 + arg2
f = FUNTYPE(function)
f(1,2)

# 还可以用这个来调用C库中的函数
# 比如：
# libm = ctypes.CDLL('libm.so.6')
# libm.cos(1.0)
# 这个和直接用 ctypes.CDLL('libm.so.6').cos(1.0) 是一样的
