import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    pass
</code>
but now I get:
<code>TypeError: an integer is required (got type generator)
</code>

