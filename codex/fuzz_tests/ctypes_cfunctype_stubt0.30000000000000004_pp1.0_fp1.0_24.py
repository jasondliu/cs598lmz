import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42
fun()

# but this is not:
@FUNTYPE
def fun():
    return "hello"
fun()
</code>

