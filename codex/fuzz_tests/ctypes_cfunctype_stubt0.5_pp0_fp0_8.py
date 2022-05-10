import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1

print(fun())
</code>
I get the following error:
<blockquote>
<p>TypeError: 'int' object is not callable</p>
</blockquote>
The documentation for <code>CFUNCTYPE</code> states that it returns a callable object, but I don't see how I'm supposed to call it.
How do I call a <code>CFUNCTYPE</code> function?


A:

<code>FUNTYPE</code> is the type of the function, not the function itself. You need to declare the function itself:
<code>fun = FUNTYPE(lambda: 1)
</code>
or
<code>fun = FUNTYPE(fun)
</code>

