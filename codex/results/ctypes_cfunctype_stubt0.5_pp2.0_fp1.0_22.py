import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42

fun.__name__ = 'fun'

print(fun.__name__)
print(fun())
</code>

