import ctypes
ctypes.cast(0, ctypes.py_object)
</code>
This is the error I get:
<code>---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
&lt;ipython-input-2-0c4b4e8eba4b&gt; in &lt;module&gt;
----&gt; 1 ctypes.cast(0, ctypes.py_object)

TypeError: cannot be converted to a pointer
</code>
However, this works:
<code>ctypes.cast(0, ctypes.c_void_p)
</code>
The error message is correct that <code>0</code> cannot be converted to a pointer. However, I would have expected <code>ctypes.py_object</code> to be an alias for <code>ctypes.c_void_p</code> (as the docs suggest), and hence the error message to be the same.
Is this a bug, or am I missing something?


A:

It looks like this is a bug in the documentation.  The <code>py_object</code> type is a
