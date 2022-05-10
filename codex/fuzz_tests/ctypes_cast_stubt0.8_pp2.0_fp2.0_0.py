import ctypes
ctypes.cast(0, ctypes.py_object)
a = ctypes.cast(0, ctypes.py_object).value
</code>
I got <code>ctypes.ArgumentError: argument 1: &lt;class 'TypeError'&gt;: wrong type</code>
I also found this post: How to set a python object to NULL (not None). But setting an object to NULL does not help me in my case since I'm not able to access the object afterwards.
Could anyone help me with this?

