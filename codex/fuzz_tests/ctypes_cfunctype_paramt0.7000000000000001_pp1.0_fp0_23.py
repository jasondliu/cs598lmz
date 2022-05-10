import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def myfunc(a):
    return a*2

fun = FUNTYPE(myfunc)
print(fun(3))
</code>
I get the error <code>TypeError: must be real number, not builtin_function_or_method</code>. I'm a bit confused because I thought <code>myfunc</code> is a function and not a method. I also don't know what a <code>builtin_function_or_method</code> is.

