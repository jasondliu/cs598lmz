import ctypes
ctypes.cast(0, ctypes.py_object).value

File "&lt;stdin&gt;", line 1, in &lt;module&gt;
ValueError: NULL pointer access
</code>
<blockquote>
<p>Why does this happen?</p>
</blockquote>
Because on a C level, <code>NULL</code> is actually just a 0 value. But when you look at this from the perspective of Python, the value becomes a null pointer.
Here's a nice blog article that discusses this in detail.

