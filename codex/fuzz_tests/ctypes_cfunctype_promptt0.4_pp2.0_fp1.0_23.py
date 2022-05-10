import ctypes
# Test ctypes.CFUNCTYPE
def my_callback(a, b):
    print "in my_callback", a, b
    return a + b

CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

lib.set_callback(CMPFUNC(my_callback))

for i in range(5):
    x = lib.call_callback(i, i+1)
    print "callback returned", x
