import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    print 'hi'
    return ctypes.py_object(None)
fun()
</code>
This will give you:
<blockquote>
<p>RuntimeError: maximum recursion depth exceeded in cmp</p>
</blockquote>
The problem is that <code>ctypes.py_object</code> tries to coerce the output to a C type. Attempting to coerce <code>None</code> to a C type results in an exception, but attempting to coerce the <code>ctypes.py_object(None)</code> that I returned will cause infinite recursion.
To see why this happens, look at the source code for the <code>py_object</code> type.
<code>def _py_object_fromaddr(addr, ptrtype):
    """
    Called by PyObj_FromPtr() and PyObj_FromPtrAndLen() - the type must
    be a pointer or a pointer-sized integer."""
    if not isinstance(ptrtype, (ctypes._Pointer, ctypes._SimpleCData)):
        raise TypeError("PyObj_FromPtr()
