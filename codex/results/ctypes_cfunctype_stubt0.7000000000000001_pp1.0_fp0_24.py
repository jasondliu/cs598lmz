import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 'bla'
</code>
But this raises an error:
<blockquote>
<p>ValueError: Procedure called with not enough arguments (2 bytes missing) or wrong calling convention</p>
</blockquote>
I don't know what is wrong here.


A:

The <code>CFUNCTYPE</code> function takes a return type followed by the types of the arguments.
<code>FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
</code>
should be
<code>FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_void_p)
</code>

