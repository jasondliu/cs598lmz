import ctypes
ctypes.cast(0, ctypes.py_object).value
</code>
<blockquote>
<p>TypeError: must be type, not int</p>
</blockquote>
<code>ctypes.cast(ctypes.c_void_p(0), ctypes.py_object).value
</code>
<blockquote>
<p>SystemError: NULL result without error in PyObject_Call</p>
</blockquote>
<code>ctypes.cast(ctypes.c_void_p(0), ctypes.py_object).value
</code>
<blockquote>
<p>SystemError: NULL result without error in PyObject_Call</p>
</blockquote>
<code>ctypes.cast(ctypes.c_void_p(0), ctypes.py_object).value
</code>
<blockquote>
<p>SystemError: NULL result without error in PyObject_Call</p>
</blockquote>
<code>ctypes.cast(ctypes.c_void_p(0), ctypes.py_object).value
</code>
