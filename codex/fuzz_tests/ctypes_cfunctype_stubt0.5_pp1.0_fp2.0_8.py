import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello world"
print fun()

# 这种方式也可以直接用ctypes.pythonapi模块来调用，如下：
import ctypes
ctypes.pythonapi.Py_InitModule4.restype = ctypes.py_object
ctypes.pythonapi.Py_InitModule4.argtypes = [ctypes.c_char_p, ctypes.py_object, ctypes.c_char_p, ctypes.py_object, ctypes.c_int]
module = ctypes.pythonapi.Py_InitModule4("hello", None, "hello world", None, 1013)
print module

# 在Python中，一个函数可以接受可变数量的参数，例如：
def func(a, b, c, d):
    print a, b, c, d
func(1, 2
