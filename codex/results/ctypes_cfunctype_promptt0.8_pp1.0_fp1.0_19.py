import ctypes
# Test ctypes.CFUNCTYPE()
def foo(x):
    print "foo(", x, ")"
    return x + 1

callback = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(foo)
print "callback(42) == %d" % callback(42)
