import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    print('hello world')
    return 'from c'

# 第二个参数是函数指针
