import ctypes
ctypes.cast(p, ctypes.py_object).value

# OUT: {'a': 1, 'b': 2}
</code>
<code>ctypes.cast</code> can also be used to convert from <code>ctypes.py_object</code> to any pointer type:
<code>&gt;&gt;&gt; ctypes.cast(ctypes.py_object(p), ctypes.POINTER(Dictionary))

# OUT: &lt;ctypes.LP_LP_Dictionary object at 0x7f9e2c3f7e58&gt;
</code>

