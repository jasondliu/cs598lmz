import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def callback_func(a, b):
    print "in python callback: a = %d, b = %d" % (a, b)
    return a + b

callback = FUNTYPE(callback_func)

print "before call"
testlib.call_callback(callback)
print "after call"
