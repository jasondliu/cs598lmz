import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def add(x, y):
    return x + y

f = FUNTYPE(add)
result = f(1, 2)
print(result)

# 创建一个高阶函数
def apply(func, *args):
    return func(*args)

result = apply(f, 3, 4)
print(result)

# 通过ctypes.pythonapi调用Python接口
# 这里的Py_BuildValue()是一个Python的C接口，用来把Python对象转换为C对象
# 如果调用失败，会抛出ctypes.ArgumentError异常

import ctypes
import sys

PyObject_GetAttrString = ctypes.pythonapi.Py
