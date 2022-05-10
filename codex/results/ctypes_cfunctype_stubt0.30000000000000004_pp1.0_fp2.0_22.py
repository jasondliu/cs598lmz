import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

print(fun())

# 下面是一个简单的例子，定义一个函数，返回一个字符串

# 定义一个函数类型
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_char_p)

# 定义一个C函数
@FUNTYPE
def fun():
    return b"hello"

# 调用这个函数
print(fun())

# 下面是一个简单的例子，定义一个函数，返回一个整数

# 定义一个函数类型
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int)

#
