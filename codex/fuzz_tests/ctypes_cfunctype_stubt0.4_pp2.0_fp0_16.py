import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42

print(fun())
</code>
This works in CPython, but not in PyPy.

