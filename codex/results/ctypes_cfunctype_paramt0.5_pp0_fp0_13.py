import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def callback_func(a, b):
    print("callback_func", a, b)
    return a + b

callback_func_type = FUNTYPE(callback_func)

# 定义回调函数
CALLBACK = FUNTYPE(None, ctypes.c_int, ctypes.c_int, ctypes.c_int)

# 定义一个函数指针
sum_func = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

# 将Python的函数转换为C的函数
sum_func_c = sum_func(callback_func)

# 定义C的函数
@CALLBACK
def py_func(a, b, sum_func):
    print("py_func", a, b)
