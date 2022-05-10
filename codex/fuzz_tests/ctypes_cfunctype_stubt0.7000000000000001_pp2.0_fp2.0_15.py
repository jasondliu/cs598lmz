import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "blah"

fun.argtypes = [ctypes.py_object]
fun.restype = ctypes.py_object

a = fun()
print(a)
</code>
This should be enough to get you started. You can get more information about the <code>ctypes</code> module here.

