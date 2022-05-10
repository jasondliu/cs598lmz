import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def myfunc(arg):
    return arg + 1

myfunctype = FUNTYPE(myfunc)

print myfunctype(5)

# output:
# 6
</code>

