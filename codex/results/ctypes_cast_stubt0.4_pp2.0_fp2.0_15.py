import ctypes
ctypes.cast(0, ctypes.py_object).value

# this call will fail
ctypes.cast(0, ctypes.py_object).value

# but this one will succeed
ctypes.cast(0, ctypes.py_object).value
</code>
Is this a bug in ctypes?


A:

I don't think this is a bug.  The first call to <code>ctypes.cast(0, ctypes.py_object).value</code> is a valid call, but the <code>value</code> attribute is not a property, so it is not called.  The second call is not valid, since the <code>value</code> attribute is not a property, so it is not called.  The third call is valid, and the <code>value</code> attribute is a property, so it is called.

