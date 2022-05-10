import ctypes
ctypes.cast(0, ctypes.py_object)
</code>
Then, I get (as expected):
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
ValueError: NULL pointer access
</code>
while the following code works on CPython (I know this is undefined behavior):
<code>&gt;&gt;&gt; import ctypes
&gt;&gt;&gt; ctypes.cast(0, ctypes.py_object).value
0
</code>
Do you have any idea what could be wrong?


A:

The problem is that <code>PyObject*</code> is expected to be a valid pointer. Since the <code>int_</code> subtype is not used to represent a pointer, it's not initialized to a valid pointer value before being passed to the function.
Since this is a bug in the implementation of <code>int_</code>, it cannot be fixed in <code>PyPy</code>.

