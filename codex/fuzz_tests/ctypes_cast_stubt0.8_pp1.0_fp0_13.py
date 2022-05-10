import ctypes
ctypes.cast(obj, ctypes.py_object).value

x = ctypes.py_object()
x.value = obj
</code>
The first form returns a new reference and <code>x.value</code> is a borrowed reference:
<code>&gt;&gt;&gt; import ctypes
&gt;&gt;&gt; ctypes.cast(obj, ctypes.py_object).value
'hello'
</code>

