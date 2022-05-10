import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 2
ctypes.addressof(fun)
</code>
<code>addressof()</code> is only allowed on C type instances.
<code>ctypes.cast(fun, ctypes.POINTER(ctypes.c_void_p)).contents
</code>
<code>ctypes.cast()</code> only works on values of C types.
<code>ctypes.cast(ctypes.py_object(fun), ctypes.POINTER(ctypes.c_void_p)).contents
</code>
<code>ctypes.py_object()</code> is only allowed on values of C types.
<code>ctypes.cast(ctypes.py_object(ctypes.c_void_p.from_address(id(fun))),
    ctypes.POINTER(ctypes.c_void_p)).contents
</code>
Finally, this does the trick:
<code>&gt;&gt;&gt; ctypes.cast(ctypes.py_object(ctypes.c_void_p.from_address(id(
