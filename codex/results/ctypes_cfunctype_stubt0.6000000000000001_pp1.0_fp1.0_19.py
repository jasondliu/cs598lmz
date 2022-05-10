import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "abc"
</code>
Now <code>fun()</code> has <code>__class__</code> <code>&lt;type 'builtin_function_or_method'&gt;</code> and <code>__name__</code> <code>'fun'</code>, but <code>'fun'</code> is not in <code>globals()</code>.

