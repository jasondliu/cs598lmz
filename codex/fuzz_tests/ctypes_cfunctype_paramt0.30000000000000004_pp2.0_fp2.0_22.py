import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def func(a, b):
    return a+b

func_c = FUNTYPE(func)

print(func_c(1, 2))

# 将python的函数绑定到C的函数指针上
# 将C的函数指针绑定到python的函数上
# 将python的函数绑定到C的函数指针上
# 将C的函数指针绑定到python的函数上
# 将python的函数绑定到C的函数指针上
# 将C的函数指针绑定到python的函数上
# 将python的函
