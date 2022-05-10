import ctypes
ctypes.cast(ctypes.c_void_p(0x1), ctypes.py_object)
</code>
This raises a <code>Segmentation fault: 11</code> on my machine.
<code>&gt;&gt;&gt; ctypes.cast(ctypes.c_void_p(0x1), ctypes.py_object)
Segmentation fault: 11
</code>
But it works if I use a pointer to a valid object:
<code>&gt;&gt;&gt; p = ctypes.py_object(1)
&gt;&gt;&gt; ctypes.cast(ctypes.c_void_p(id(p)), ctypes.py_object)
&lt;ctypes.py_object object at 0x10f9d5b20&gt;
</code>
I'm not sure what's going on here. Why does the cast work on a pointer to a valid object, but not on a pointer to an invalid object?

