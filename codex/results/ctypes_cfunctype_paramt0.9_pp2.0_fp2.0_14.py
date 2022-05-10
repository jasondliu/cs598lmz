import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None,ctypes.py_object)
type( FUNTYPE )

def callback_func(x):
    print >> sys.stderr, "CALLBACK", x

ccall = ctypes.ap
