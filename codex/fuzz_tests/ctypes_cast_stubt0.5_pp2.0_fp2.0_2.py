import ctypes
ctypes.cast(0, ctypes.py_object)
# Segmentation fault
</code>
I am using python 3.7.0.
What is the problem?


A:

It is because you are using a 64-bit version of Python, and <code>ctypes</code> is trying to cast a <code>long</code> to a <code>PyObject</code>.
<code>&gt;&gt;&gt; type(0)
&lt;class 'int'&gt;
&gt;&gt;&gt; type(0L)
&lt;class 'long'&gt;
</code>
You can fix this by using a 32-bit version of Python.

