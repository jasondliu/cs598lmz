import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def func(n):
    print("func called with %d" % n)
    return n + 1

f = FUNTYPE(func)

f(1)

# 使用ctypes.pythonapi调用python的函数
# pythonapi是一个动态链接库，里面包含了很多python的C API
# 可以通过ctypes.pythonapi.PyObject_CallObject调用python的函数

import ctypes
import sys

# 定义一个python的函数
def func(n):
    print("func called with %d" % n)
    return n + 1

# 获取pythonapi
pythonapi = ctypes.pythonapi

# 获取python的函数类型
PyObject_CallObject = pythonapi.PyObject_
