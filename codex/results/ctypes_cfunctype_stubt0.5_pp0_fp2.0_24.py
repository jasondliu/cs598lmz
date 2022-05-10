import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

print(fun())
</code>
This code works, but it is not what I want.
I want to use fun() in another function:
<code>def fun2():
    return fun
</code>
But then the error occurs:
<code>def fun2():
    return fun

print(fun2())
</code>
<blockquote>
<p>TypeError: 'CFUNCTYPE' object is not callable</p>
</blockquote>
I know I can use <code>ctypes.cast</code> to cast the function pointer to a function type, but I am not sure how to do it.
I have tried the following code:
<code>def fun2():
    return ctypes.cast(fun, FUNTYPE)
</code>
But it doesn't work.
<blockquote>
<p>TypeError: must be convertible to a pointer</p>
</blockquote>
I have also tried:
<code>def fun2():
    return ctypes.cast(ctypes.pointer(fun), FUNTYPE)
</code>
