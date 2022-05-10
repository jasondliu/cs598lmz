import ctypes
ctypes.cast(ctypes.c_char_p(s), ctypes.POINTER(ctypes.c_char * 2))
</code>
But I get an error:
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
TypeError: must be a pointer-to-GObject subclass
</code>
What am I doing wrong?


A:

I know nothing about ctypes, but I think you're trying to cast a char pointer to a pointer to a pointer to a char.
<code>ctypes.cast(ctypes.c_char_p(s), ctypes.POINTER(ctypes.POINTER(ctypes.c_char)))</code>

