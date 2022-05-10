import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
def myfunc(i):
    return i + 10

cfunc = FUNTYPE(myfunc)
print(cfunc(10))

# 创建一个类
class MyFunc:
    def __init__(self):
        self.value = 0
    def myfunc(self, i):
        self.value = i + 10
        return self.value

myfunc = MyFunc()
cfunc = FUNTYPE(myfunc.myfunc)
print(cfunc(10))
print(myfunc.value)

# 把函数转换为可以使用ctypes.cdll.LoadLibrary()加载的函数
from ctypes import *

libc = CDLL("libc.so.6")

# 这里的libc.printf 是一个原型为 int printf(const char *format, ...)的函数
#
