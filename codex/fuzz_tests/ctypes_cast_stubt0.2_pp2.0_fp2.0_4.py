import ctypes
ctypes.cast(0, ctypes.py_object).value

# Output:
# Traceback (most recent call last):
#   File "&lt;stdin&gt;", line 1, in &lt;module&gt;
# ValueError: NULL pointer access
</code>

