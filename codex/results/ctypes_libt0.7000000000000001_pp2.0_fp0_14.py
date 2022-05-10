import ctypes
ctypes.c_ushort(-1)
</code>
Gives the following traceback:
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
OverflowError: Python int too large to convert to C unsigned short
</code>
However, the following works:
<code>import ctypes
ctypes.c_ulong(-1)
</code>
So, is there a way to represent the max int that can be stored in a ushort (65535) in python?


A:

<blockquote>
<p>So, is there a way to represent the max int that can be stored in a ushort (65535) in python?</p>
</blockquote>
Sure, just use <code>65535</code>:
<code>&gt;&gt;&gt; x = ctypes.c_ushort(65535)
&gt;&gt;&gt; x
c_ushort(65535)
</code>

<blockquote>
<p>I
