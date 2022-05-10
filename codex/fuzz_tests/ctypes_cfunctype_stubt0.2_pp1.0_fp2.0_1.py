import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

fun()

# This is the same as:

def fun():
    return "hello"

ctypes.pythonapi.PyCFunction_NewEx(FUNTYPE, fun, None, None)
</code>

