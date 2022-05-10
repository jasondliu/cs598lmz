import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "str"

print(fun())
</code>
Output:
<code>str
</code>

