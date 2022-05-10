import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1
fun()

# 方法二：
import ctypes
def fun():
    return 1
