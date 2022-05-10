import ctypes
ctypes.cast(x, ctypes.py_object).value
</code>
Here's an example to demonstrate how this works:
<code>&gt;&gt;&gt; import dis
&gt;&gt;&gt; import ctypes
&gt;&gt;&gt; a = ctypes.cast(id(dis), ctypes.py_object).value
&gt;&gt;&gt; a
&lt;module 'dis' from '/System/Library/Frameworks/Python.framework/Versions/3.4/lib/python3.4/dis.py'&gt;
&gt;&gt;&gt; import dis
&gt;&gt;&gt; b = ctypes.cast(id(dis), ctypes.py_object).value
&gt;&gt;&gt; a == b
True
</code>

