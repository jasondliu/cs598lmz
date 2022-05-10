import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return b'\x00\x01'

print(fun())
</code>
the output is:
<code>b'\x00\x01'
</code>
The function return the bytes object. The function is written in C.

