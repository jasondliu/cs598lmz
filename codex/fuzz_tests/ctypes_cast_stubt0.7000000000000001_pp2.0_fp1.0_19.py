import ctypes
ctypes.cast(id(int), ctypes.py_object).value
</code>
Is there a built-in way to do the same thing?


A:

The Python object corresponding to a C <code>PyObject</code> is available as the <code>python_object</code> attribute of the object:
<code>&gt;&gt;&gt; x = ctypes.py_object(42)
&gt;&gt;&gt; x.python_object
42
</code>

