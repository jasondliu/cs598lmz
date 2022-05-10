import ctypes
ctypes.cast(1, ctypes.py_object)

# 使用ctypes模块创建一个C语言的数组
from ctypes import *
array_1 = (c_int * 3)()
array_1[0] = 1
array_1[1] = 2
array_1[2] = 3
print(array_1[0], array_1[1], array_1[2])

# 使用ctypes模块创建一个C语言的结构体
from ctypes import *
class Bar(Structure):
    _fields_ = [("a", c_int), ("b", c_int)]

bar = Bar(1, 2)
print(bar.a, bar.b)

# 使用ctypes模块创建一个C语言的共享库
from ctypes import *
lib = CDLL("./lib
