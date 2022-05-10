import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1
fun()
</code>
The error is:
<code>OverflowError: cannot convert float infinity to integer
</code>
I think it is because ctypes doesn't support return type <code>ctypes.py_object</code>, but I can't find the documentation about this.
Is there any way to return Python object from a ctypes function?

