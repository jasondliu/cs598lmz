import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    print "Hello %s" % ctypes.py_object(fun)
fun()
</code>

