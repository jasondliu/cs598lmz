import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def callback(i):
    print "callback is called with: ", i
    return i * 2

lib = ctypes.CDLL('libtest.so')

# must assign the function to a global variable
py_cb = FUNTYPE(callback)

lib.register_callback(py_cb)

lib.call_callback(3)
