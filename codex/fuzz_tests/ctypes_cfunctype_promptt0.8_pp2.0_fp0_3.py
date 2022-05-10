import ctypes
# Test ctypes.CFUNCTYPE by creating a function that calls back to
# Python.  This is a rather contrived example, but it is effective.

callback = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def py_callback(a, b):
    # Python callback, called from C
    print "python callback", a, b # user code
    return a + b

c_callback = callback(py_callback)

#lib = ctypes.CDLL('./test.so')
lib.pycallback(2, 3, c_callback)
# prints "python callback 2 3"
# returns 5
