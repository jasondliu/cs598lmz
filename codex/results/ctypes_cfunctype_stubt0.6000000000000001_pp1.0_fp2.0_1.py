import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    pass
print(fun)
</code>
This is interpreted as <code>fun = FUNTYPE(lambda: None)</code> which is equivalent to the above.

