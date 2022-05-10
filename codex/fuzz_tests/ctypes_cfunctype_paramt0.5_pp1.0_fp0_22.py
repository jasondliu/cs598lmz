import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
c_sum = FUNTYPE(sum)
print(c_sum(1, 2))

# Python 函数作为参数传递给C函数
# 定义一个C函数
# int call(int(*func)(int, int), int a, int b)
# {
#     return func(a, b);
# }

# 声明一个C函数
# int call(int(*func)(int, int), int a, int b);
# 将Python函数转换为C函数指针
# cfunc = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)(sum)
# 调用C函数
# call(cfunc, 1, 2)

# C函数库

