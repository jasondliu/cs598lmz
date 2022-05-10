import ctypes
ctypes.cast(hex(int(hex(id(obj)),16) + 16), ctypes.py_object).value
</code>
However, I cannot get it to run in Python 3.
<blockquote>
<p>TypeError: an integer is required (got type str)</p>
</blockquote>
As I understand it, this is because the Python 3 <code>id()</code> function returns a <code>Py_ssize_t</code> (a signed long, which is 8 bytes), while the Python 2 <code>id()</code> function returns a pointer (unsigned 4 bytes).
How can I modify this code to work in Python 3?

