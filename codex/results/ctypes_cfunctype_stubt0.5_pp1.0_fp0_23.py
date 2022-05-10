import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42

print fun()
</code>
This is a very simple example, but it should give you a good starting point.

