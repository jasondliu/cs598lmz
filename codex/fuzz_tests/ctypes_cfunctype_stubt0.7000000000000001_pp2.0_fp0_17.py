import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 7
</code>
But I can't figure out how to get the ctypes function pointer (the one in the 'address' attribute) out of the function object.
Is it possible to do this?
The documentation for ctypes.FunctionType says:
<code>class ctypes.FunctionType(restype, argtypes, *,
                          use_errno=False, use_last_error=False)
</code>
<blockquote>
<p>Creates a Python function object from C callable. </p>
<p>The function object is callable and when called it invokes the function
  given by restype(*argtypes)(*args, **kwds). </p>
<p>The arguments restype and argtypes
  are the same as in CFUNCTYPE().</p>
</blockquote>
But there's no mention of any other arguments the constructor might take.

