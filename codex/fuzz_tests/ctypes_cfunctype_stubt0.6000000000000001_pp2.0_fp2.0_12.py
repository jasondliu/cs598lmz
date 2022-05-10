import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return [1,2,3]

print(fun()[0])
</code>
Output:
<code>1
</code>

