import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1

fun()
</code>
This code works, but I am not sure whether I am doing it right. I am wondering whether there is a better way to do this.

