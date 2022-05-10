import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 0

fun()
</code>
works (Python 2.7 and Python 3.3)

