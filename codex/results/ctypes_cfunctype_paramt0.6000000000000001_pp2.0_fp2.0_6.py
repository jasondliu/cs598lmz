import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_char_p)

def _callback(msg):
    print "Callback: %s" % msg
    return 0

_callback_func = FUNTYPE(_callback)

# Load the shared library into ctypes
_test = ctypes.CDLL('./_test.so')

# Set the argtypes and restype on the C func
_test.test.argtypes = (FUNTYPE,)
_test.test.restype = ctypes.c_int

# Call the C function via ctypes
_test.test(_callback_func)
</code>

