import ctypes
ctypes.cast(p, ctypes.py_object).value
</code>
This works because <code>ctypes.cast(p, ctypes.py_object).value</code> is a PyObject* that points to the same object as <code>p</code>.  Then <code>ctypes.py_object(p)</code> creates a Python object from the PyObject*.
<code>&gt;&gt;&gt; p = ctypes.py_object(1)
&gt;&gt;&gt; ctypes.cast(p, ctypes.py_object).value is p
True
</code>

