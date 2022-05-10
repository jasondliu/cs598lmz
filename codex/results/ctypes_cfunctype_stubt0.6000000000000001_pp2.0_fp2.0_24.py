import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1

print(fun())
</code>
This program prints:
<code>1
</code>
However, if you change the return type of <code>fun</code> to <code>int</code>, you get:
<code>TypeError: an integer is required (got type _ctypes.PyCapsule)
</code>
This happens because the C function returns a PyCapsule, which Python can't interpret as an int.

