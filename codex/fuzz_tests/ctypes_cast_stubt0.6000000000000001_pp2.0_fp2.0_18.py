import ctypes
ctypes.cast('i', 'd')

&gt;&gt;&gt; ctypes.cast('i', 'd')
Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
TypeError: must be string or read-only buffer, not type
</code>


A:

The <code>ctypes.cast</code> function is used to convert between different ctypes types.  You can use it to convert between <code>c_void_p</code> and a ctypes type which is a pointer to an object, but you can't use it to convert between pointers to different objects.
You can use <code>ctypes.cast</code> to convert between integer types.  Here are some examples:
<code>&gt;&gt;&gt; import ctypes
&gt;&gt;&gt; ctypes.cast(ctypes.c_int(42), ctypes.c_char)
&lt;ctypes.c_char object at 0x10f619e40&gt;
&gt;&gt
