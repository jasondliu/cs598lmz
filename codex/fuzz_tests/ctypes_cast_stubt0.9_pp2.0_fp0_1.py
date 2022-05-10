import ctypes
ctypes.cast(0, ctypes.py_object)
</code>
Now this raises a <code>ValueError</code>:
<blockquote>
<p>ValueError: NULL pointer access</p>
</blockquote>
which means, <code>ctypes</code> is not able to cast 0 to a memory address to create an object. For this reason even if you're able to create <code>None</code> inside a function, you won't be able to access it outside.
Also, this approach is bound to fail even if you manage to create it inside the function:
<code>&gt;&gt;&gt; a = do_nothing()
&gt;&gt;&gt; import ctypes
&gt;&gt;&gt; ctypes.cast(a, ctypes.py_object)
Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
  File "ctypes/__init__.py", line 361, in cast
    return self._cast(obj, self)
ctypes.ArgumentError: argument
