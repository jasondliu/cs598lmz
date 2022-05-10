import ctypes
ctypes.cast(2, ctypes.c_void_p)
</code>
<code>ctypes.cast</code> doesn't work with values of type <code>int</code>, because they are not C pointers.
<code>&gt;&gt;&gt; ctypes.cast(2, ctypes.c_void_p)
Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
TypeError: expected LP_c_void instance instead of int
</code>

