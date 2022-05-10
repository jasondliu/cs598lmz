import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42

print(fun())
</code>
It works as expected on Windows, but on Linux it raises <code>Segmentation fault</code>.
I tried to use <code>ctypes.CFUNCTYPE(ctypes.c_int)</code> instead of <code>ctypes.CFUNCTYPE(ctypes.py_object)</code> and it works.
Why does it happen?

