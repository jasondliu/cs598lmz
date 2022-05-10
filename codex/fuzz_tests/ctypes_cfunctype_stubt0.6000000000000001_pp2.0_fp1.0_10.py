import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return None
</code>
When I run <code>fun()</code> (or <code>fun</code>), I get the following error:
<code>TypeError: Required argument 'self' (pos 1) not found
</code>
I'm using Python 2.7 on Windows 7.


A:

The <code>CFUNCTYPE</code> class is used to define callback functions that can be called by the C code you're interfacing with.
You are not defining a callback function, you are defining a Python function. For that, use <code>types.FunctionType</code>:
<code>import types

FUNTYPE = types.FunctionType
@FUNTYPE
def fun():
    return None
</code>

