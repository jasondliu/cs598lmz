import ctypes
# Test ctypes.CFUNCTYPE, ctypes.c_int, ctypes.c_char_p, ctypes.c_void_p

# This is the prototype of the function we want to call
PROTO = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_char_p, ctypes.c_void_p)

# This is the function we want to call
def func(name, param):
    print "func(%s, %s)" % (name, param)
    return 42

# This is the address of the function we want to call
addr = ctypes.cast(func, ctypes.c_void_p).value

# This is the address of the prototype of the function we want to call
proto = ctypes.cast(PROTO, ctypes.c_void_p).value

# This is the address of the function we want to call, cast to the correct type
f = ctypes.cast(addr, PROTO)

# Call the function
print f("hello", None)

# Call the function, using the address of the prototype
print ctypes
