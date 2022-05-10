import ctypes
# Test ctypes.CFUNCTYPE()
print
print "call a callback with a string parameter"
CB_FUNC = ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_char_p)
def my_callback(msg):
    print "callback:", msg
cb = CB_FUNC(my_callback)
cb("hello")

# Test keyword argument with out value
C
