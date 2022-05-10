import ctypes
ctypes.cast('A', ctypes.c_char_p)
Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
TypeError: cast() argument 2 must be a pointer type, not str
</code>
But using strings took care of the problem:
<code>&gt;&gt;&gt; import ctypes
&gt;&gt;&gt; b'A'
b'A'
&gt;&gt;&gt; b'A'[0]
65
&gt;&gt;&gt; ctypes.c_char_p(b'A'[0])
c_char_p(65)
&gt;&gt;&gt; ctypes.cast(b'A'[0], ctypes.c_char_p)
c_char_p(65)
</code>
I had already understood the problem, though. I tried to simplify my code and found that I can use <code>bytes</code> values:
<code>ctypes.cast(bytes(1), ctypes.
