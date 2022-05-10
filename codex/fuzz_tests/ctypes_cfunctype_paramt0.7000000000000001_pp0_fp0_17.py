import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def func(a, b):
    print("func ", a, b)
    return a + b

# 将func函数转换为CFUNCTYPE函数类型
CFUNC = FUNTYPE(func)
print(CFUNC)
# 将CFUNC保存在lib中
lib = ctypes.CDLL("./libfunc.so")
# 将CFUNC的地址付给lib中的变量
lib.set_func(CFUNC)
# 调用lib中的函数，调用CFUNC
print(lib.call_func(2, 3))
