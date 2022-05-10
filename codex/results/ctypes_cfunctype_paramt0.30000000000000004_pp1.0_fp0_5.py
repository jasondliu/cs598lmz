import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def myfunc(x):
    return x

f = FUNTYPE(myfunc)

print f(2)

# this is a function pointer
print f

# this is the address of the function
print ctypes.addressof(f.__closure__[0])
</code>

