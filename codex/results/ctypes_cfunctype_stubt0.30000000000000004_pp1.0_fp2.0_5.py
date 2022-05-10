import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

print(fun())

# 将python的函数转换为c的函数
def fun2(x,y):
    return x+y

cfun = FUNTYPE(fun2)
print(cfun(1,2))

# 将c的函数转换为python的函数
import ctypes
lib = ctypes.cdll.LoadLibrary("./libtest.so")
cfun = lib.fun
cfun.restype = ctypes.py_object
print(cfun())
