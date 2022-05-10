import ctypes
ctypes.cast(0, ctypes.py_object).value

# 使用ctypes模块访问C语言的动态链接库
# 在Python中调用C语言的动态链接库，可以使用ctypes模块
# 使用ctypes模块访问C语言的动态链接库，需要先导入ctypes模块，然后使用ctypes.cdll.LoadLibrary()函数加载动态链接库，
# 再使用函数名调用C语言的函数。
# 如果C语言的函数返回
