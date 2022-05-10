import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def my_func(a, b):
    return a + b

my_func_c = FUNTYPE(my_func)

print(my_func_c(1, 2))

# 定义一个回调函数
def callback(a, b):
    print("callback called with %d and %d" % (a, b))
    return a + b

# 将回调函数转换为C函数指针
callback_c = FUNTYPE(callback)

# 定义一个C函数
libc = ctypes.CDLL(None)
libc.my_function.argtypes = (ctypes.c_int, ctypes.c_int, FUNTYPE)
libc.my_function.restype = ctypes.c_int

# 调用C函数
print(lib
