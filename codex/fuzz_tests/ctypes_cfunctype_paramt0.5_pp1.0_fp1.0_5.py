import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def myfunc(x):
    print x
    return x

cfunc = FUNTYPE(myfunc)
cfunc(3)
</code>
This works fine, however, I would like to pass a pointer to a function as a parameter to another ctypes function. I'm not sure how to do this.
For example, I would like to do something like this:
<code>mylib.myCfunction(cfunc)
</code>
where <code>mylib.myCfunction</code> is a ctypes function.
How do I do this?


A:

You need to use <code>ctypes.cast</code> to cast the function pointer to the right type.
<code>mylib.myCfunction(ctypes.cast(cfunc, ctypes.c_void_p))
</code>

