import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def func(x):
    return x**2

f = FUNTYPE(func)
print f(1.0)
</code>
This works fine, but if I try to pass a function with a default argument, I get a TypeError:
<code>def func(x, y=1):
    return x**y

f = FUNTYPE(func)
</code>
<blockquote>
<p>TypeError: argument 1: : Don't know how to convert parameter 1</p>
</blockquote>
I've tried a few things, but I can't figure out how to get it to work.


A:

You need to define a new <code>FUNTYPE</code> with a second argument:
<code>FUNTYPE2 = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double)
f = FUNTYPE2(func)
</code>

