import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

# define function
def myfunc(a, b):
    return a + b

# convert function to ctypes pointer
cfunc = FUNTYPE(myfunc)

# call function
print(cfunc(1, 2))

# call function with pointer
print(cfunc.__call__(1, 2))
</code>
This is the output:
<code>3
3
</code>

