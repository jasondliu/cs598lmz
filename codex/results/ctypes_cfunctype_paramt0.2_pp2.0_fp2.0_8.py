import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def func(a, b):
    return a + b

func_ptr = FUNTYPE(func)
print(func_ptr(1, 2))

# 将函数指针作为参数传递给C函数
# 定义一个C函数
libc = ctypes.CDLL(None)
c_func = libc.printf
c_func.argtypes = (ctypes.c_char_p, FUNTYPE)
c_func.restype = ctypes.c_int

# 将函数指针作为参数传递给C函数
c_func("%d\n", func_ptr)

# 将函数指针作为返回值返回
c_func = libc.strstr
c
