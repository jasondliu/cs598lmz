import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int)
def py_mytest(i,j):
    print (i,j)
    return(i+j)

add_int = FUNTYPE(('add', globals()))

print(add_int(1,2))
</code>
I thought this should work but it isn't.
How can I call a function that is in a module imported dynamically with ctypes?


A:

You can't.
A <code>ctypes.CFUNCTYPE</code> instance is initialized with a callback function pointer. It can't call a Python callable. 

