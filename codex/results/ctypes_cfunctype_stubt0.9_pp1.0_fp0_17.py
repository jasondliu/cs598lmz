import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1
x = fun()
print(x)
</code>
Output:
<code>1
</code>

