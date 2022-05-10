import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1234567890
print fun()
</code>
and it yields <code>1234567890</code> as expected.

