import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"
print(fun())

# 将python函数转换为c函数
import ctypes
def fun():
    return "hello"
fun_c = ctypes.CFUNCTYPE(ctypes.c_char_p)(fun)
print(fun_c())
