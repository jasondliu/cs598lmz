import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "Hello from C"

print(fun())
</code>
Note that this only works on CPython. Running this code with PyPy will crash the interpreter.

