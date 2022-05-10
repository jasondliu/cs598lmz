import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "Hello"
</code>
I get the error:
<code>TypeError: 'CFUNCTYPE' object cannot be used in 'await' expression
</code>
I'm using Python 3.7.3.


A:

The <code>async def</code> syntax is a short-hand for creating <code>async</code>-compatible functions.  It's not a way to make a function that wasn't already <code>async</code>-compatible into an <code>async</code> function.
You can't <code>await</code> a function that isn't <code>async</code>.  It's not that it's impossible to make a C function <code>async</code>-compatible, it's that the <code>async def</code> syntax is not the way to do it.

