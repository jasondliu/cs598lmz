import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
def c_function(a,b):
    return a + b

cfunc = FUNTYPE(c_function)
print cfunc(1,1)
</code>
This gives the following error:
<code>TypeError: The second argument must be a callable
</code>
What does this message mean? How can I fix this?


A:

The Python documentation for ctypes says that the second argument to <code>CFUNCTYPE</code> must be a "callable object" (the object returned from <code>cfunc</code> is not callable).
Try this:
<code>&gt;&gt;&gt; from ctypes import CFUNCTYPE, c_int
&gt;&gt;&gt; def c_function(a, b):
...   return a + b
...
&gt;&gt;&gt; cfunc = CFUNCTYPE(c_int, c_int, c_int)(c_function)
&gt;&gt
