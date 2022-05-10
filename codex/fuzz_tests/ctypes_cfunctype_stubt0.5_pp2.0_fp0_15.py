import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42
print(fun())
print(fun() == 42)
</code>
Output:
<code>42
True
</code>

