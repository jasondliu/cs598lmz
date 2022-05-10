import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int,ctypes.c_int,ctypes.c_int)

def py_callback(arg1,arg2):
    print "Python callback called with",arg1,arg2
    return 42

callback = FUNTYPE(py_callback)

libc.callback_with_callback(callback)
</code>

