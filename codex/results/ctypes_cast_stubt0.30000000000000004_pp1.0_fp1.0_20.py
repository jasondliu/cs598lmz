import ctypes
ctypes.cast(0, ctypes.py_object).value

# 使用ctypes调用C函数
import ctypes

# 定义C函数
def c_func(a, b):
    return a + b

# 将C函数转换为ctypes可调用的函数
c_func_type = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
c_func_callable = c_func_type(c_func)

# 调用C函数
c_func_callable(1, 2)

# 使用ctypes调用C函数
import ctypes

# 定义C函数
def c_func(a, b):
    return a + b

# 将C函数转换为ctypes可调用
