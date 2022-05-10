import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42
try:
    fun()
except TypeError:
    print("TypeError")

@FUNTYPE
def fun():
    return 42.
try:
    fun()
except TypeError:
    print("TypeError")

@FUNTYPE
def fun():
    return "42"
fun()
