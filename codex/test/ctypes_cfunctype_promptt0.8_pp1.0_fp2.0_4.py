import ctypes
# Test ctypes.CFUNCTYPE
def baz(x, y):
    return x, y

PFUN = ctypes.CFUNCTYPE(ctypes.c_int,   # return type
                        ctypes.c_int,   # arg1 type
                        ctypes.c_int)   # arg2 type

# Now create an instance of the function
pfun = PFUN(baz)

# Use it!
print(pfun(3,4))

