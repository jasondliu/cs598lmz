import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    print "hi"
    return "hi"
</code>
I get a segfault. What am I doing wrong?

