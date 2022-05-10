import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_int, ctypes.c_int)

def func(x,y):
    return x + y

cfunc = FUNTYPE(func)

cfunc(1,2)
</code>
But I get the following error:
<code>TypeError: expected CFUNCTYPE instance instead of function
</code>
I understand that <code>ctypes.CFUNCTYPE</code> expects a function as an argument, but I don't understand why it is not working. 
It is the same as in this answer:
https://stackoverflow.com/a/11120847/1688441


A:

You need to instantiate <code>CFUNCTYPE</code> with the function's argtypes and restype.
<code>cfunc = FUNTYPE((ctypes.c_int, ctypes.c_int), ctypes.c_double)(func)
</code>

