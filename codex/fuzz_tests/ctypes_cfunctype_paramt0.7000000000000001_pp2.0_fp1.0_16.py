import ctypes
FUNTYPE = ctypes.CFUNCTYPE(
    ctypes.c_int,              # Return type
    ctypes.c_int,              # arg1 type
    ctypes.c_int               # arg2 type
)
def wrap(func):
    return FUNTYPE(func)

# Now add it to the module
add = wrap(add)
mymod.add = add

# Test it
print(mymod.add(1, 2))

# Done!
</code>

