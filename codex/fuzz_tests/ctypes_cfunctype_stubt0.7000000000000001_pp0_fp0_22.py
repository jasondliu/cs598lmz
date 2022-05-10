import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return (1,2)

a = fun()
print a
</code>
Output:
<code>(1, 2)
</code>
I'm not sure if this is what you are looking for.

