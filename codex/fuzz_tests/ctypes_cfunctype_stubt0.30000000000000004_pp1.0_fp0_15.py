import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42
</code>
The above code works as expected.
However, if I change the function to:
<code>@FUNTYPE
def fun(x):
    return x
</code>
I get the following error:
<code>TypeError: &lt;built-in function fun&gt;: wrong number of arguments (expected 0, got 1)
</code>
I have tried to use <code>ctypes.c_void_p</code> as the argument type, but that gives me a <code>TypeError</code> as well.
I have also tried to use <code>ctypes.c_void_p</code> as the return type, but that gives me a <code>TypeError</code> as well.
Is there a way to make this work?


A:

You can't pass arguments to a <code>CFUNCTYPE</code> callback.  You can only pass a <code>void *</code> to the callback, and the callback must return a <code>void *</code>.  The <code>void *</code> is a generic pointer that you can
