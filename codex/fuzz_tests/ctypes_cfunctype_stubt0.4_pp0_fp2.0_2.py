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
ctypes.pythonapi.PyCFunction_NewEx(ctypes.pythonapi.PyMethodDef, None, None)
</code>

