import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 0

ctypes.cast(fun, ctypes.c_void_p).value

#    Output:
#    -4032604636824
</code>
If you are certain that your function pointer is 32-bit, you can cast to <code>c_uint32</code> instead.

