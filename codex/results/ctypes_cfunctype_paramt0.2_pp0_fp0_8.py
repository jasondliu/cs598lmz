import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def f(x):
    return x**2

f_c = FUNTYPE(f)

print f_c(2.0)
</code>
This works fine, but I would like to be able to pass a function that takes more than one argument.  I tried the following:
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double)

def f(x, y):
    return x**2 + y**2

f_c = FUNTYPE(f)

print f_c(2.0, 3.0)
</code>
But this gives the error:
<code>TypeError: &lt;built-in function f&gt; is not a Python function
</code>
Is there any way to do this?


A:

You can use <code>ctypes.c_double</code> as the return type, but you need to use <code>ctypes.c_void
