import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
def func(n):
    return n + 1

cfunc = FUNTYPE(func)
print(cfunc(1))

# 将函数指针作为回调函数
def callback(n):
    return n + 1

CALLBACK = FUNTYPE(callback)

def call_c_func(f, n):
    return f(n)

print(call_c_func(CALLBACK, 1))
