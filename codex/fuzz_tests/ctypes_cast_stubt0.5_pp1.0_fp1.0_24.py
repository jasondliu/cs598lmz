import ctypes
ctypes.cast(0, ctypes.py_object).value

# TypeError: NULL pointer access
#   File "&lt;stdin&gt;", line 1, in &lt;module&gt;
# TypeError: NULL pointer access
</code>
This is the same error that occurs when trying to access the value of a <code>ctypes</code> pointer without first checking that it is not <code>NULL</code>:
<code>&gt;&gt;&gt; ctypes.cast(0, ctypes.c_void_p).value

# TypeError: NULL pointer access
#   File "&lt;stdin&gt;", line 1, in &lt;module&gt;
# TypeError: NULL pointer access
</code>

