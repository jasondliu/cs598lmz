import ctypes
ctypes.cast(0, ctypes.py_object)
</code>
I got the following error.
<code>TypeError: &lt;class 'int'&gt;: don't know how to handle address
</code>
What am I missing?


A:

Consider your last line:
<code>ctypes.cast(0, ctypes.py_object)
</code>
This is a cast of the integer 0 to <code>ctypes.py_object</code>.  The error message is telling you that <code>ctypes.py_object</code> is an int.  If you do this, you'll get an int:
<code>type(ctypes.py_object)
</code>
If you want to cast the integer 0 to a Python object, you want:
<code>ctypes.cast(0, ctypes.py_object).value
</code>
But this is exactly the same as:
<code>ctypes.cast(0, ctypes.py_object).value
</code>

