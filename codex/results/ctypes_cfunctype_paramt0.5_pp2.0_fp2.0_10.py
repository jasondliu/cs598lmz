import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
def call_func(func, arg):
    return func(arg)
func = FUNTYPE(call_func)
print(func(1))

# 把Python函数转换成C函数
def add(a, b):
    return a + b
add_cfunc = FUNTYPE(add)
print(add_cfunc(1, 2))

# 回调函数
def my_callback(a):
    print("callback called with %d" % a)
    return 0
CALLBACK = FUNTYPE(my_callback)
def call_callback(cb, a):
    cb(a)
call_callback(CALLBACK, 1)

# 把C函数转换成Python函数
import sys
if sys.platform == "win32":
    import ctypes
    cdll = ctypes.CDLL("msvcrt")
    MessageBox = cdll.MessageBox
