import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1
assert fun() == 1
</code>
This works with Python 2.7, Python 3.4, and Python 3.5.

