import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"
print(fun())
# hello

# fun是一个函数，它的类型是CFUNCTYPE，它的返回值类型是py_object
print(type(fun))
# <class 'ctypes.CFUNCTYPE'>
print(fun.restype)
# <class 'ctypes.py_object'>

# 我们可以通过ctypes.cast将函数转换成指针，然后再转换成字符串
print(ctypes.cast(fun, ctypes.c_void_p).value)
# 140714254476608
print(ctypes.cast(fun, ctypes.c_void_p).value)
# 140714254476608
print(ctypes.cast(fun, ctypes.c_void_p).value)
# 1407
