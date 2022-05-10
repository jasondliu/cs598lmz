import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def func(a, b):
    return a + b

f = FUNTYPE(func)
print(f(1, 2))

# 回调函数
def func2(a, b):
    print(a, b)

f2 = FUNTYPE(func2)
f2(1, 2)

# 回调函数
def func3(a, b):
    print(a, b)

f3 = FUNTYPE(func3)
f3(1, 2)
