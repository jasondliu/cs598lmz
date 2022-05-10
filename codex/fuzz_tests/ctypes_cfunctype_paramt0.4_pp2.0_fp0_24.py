import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def func(n):
    print("Python: func({})".format(n))
    return n + 1

# Wrap func with FUNTYPE
cfunc = FUNTYPE(func)

# Call cfunc
print("Python: cfunc(42) = {}".format(cfunc(42)))
</code>
Output:
<code>Python: func(42)
Python: cfunc(42) = 43
</code>

