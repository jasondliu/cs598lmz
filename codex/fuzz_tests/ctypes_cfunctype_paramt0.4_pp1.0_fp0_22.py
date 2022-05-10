import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
def fun(x, y):
    return x + y

cfun = FUNTYPE(fun)
print(cfun(1, 2))

# 可以使用ctypes.POINTER()函数创建指针类型
# 创建一个指向函数的指针
fun_pointer = ctypes.POINTER(FUNTYPE)

# 定义一个指向函数的指针变量
callback = fun_pointer(cfun)

# 调用回调函数
print(callback(2, 3))

# 使用ctypes.CFUNCTYPE()函数创建一个回调函数
# 定义回调函数的
