import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    print "haha"

fun()
print ctypes.sizeof(fun)
print ctypes.sizeof(FUNTYPE)
</code>
But you cannot use <code>sizeof</code> with C <code>function</code> or <code>pointer</code> types.

