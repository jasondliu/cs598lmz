import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun(): return (i for i in xrange(10))
</code>
In this case, you'll have to call <code>fun</code> directly to get a generator. This is an ugly solution, but one whose implementation is clear, understandable and does not require any tangled code. You could even call <code>update({functype.__name__: fun})</code> to update the right namespace to name your generator <code>fun()</code>.

