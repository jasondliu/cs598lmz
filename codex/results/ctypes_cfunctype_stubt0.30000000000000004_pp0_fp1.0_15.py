import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 0

def call(f):
    return f()

call(fun)
</code>
This code works fine, but when I try to call the function with <code>call(fun())</code> it raises a <code>TypeError</code> saying that <code>fun()</code> is not a function.
I know that I can use <code>ctypes.cast</code> to cast the return value of <code>fun</code> to a function pointer, but I don't want to do that.
Is there a way to do this?


A:

<code>fun()</code> returns an integer, which is not a function.  You can't call an integer.
<code>call(fun())</code> is equivalent to <code>call(0)</code>.

