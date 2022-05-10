import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1
fun()

# 这个函数没有返回值，所以调用会报错
@FUNTYPE
def fun():
    return
fun()

# 使用ctypes.py_object作为返回值类型
@ctypes.CFUNCTYPE(ctypes.py_object)
def fun():
    return 1
fun()

# 使用ctypes.py_object作为返回值类型，这个函数没有返回值，所以调用会报错
@ctypes.CFUNCTYPE(ctypes.py_object)
def fun():
    return
fun()

# 使用ctypes.py_object作为返回值类型，
