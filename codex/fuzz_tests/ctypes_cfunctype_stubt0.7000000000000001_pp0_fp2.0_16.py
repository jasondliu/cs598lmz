import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    print(a)
    return a

fun()
</code>
Output:
<code>1
</code>

