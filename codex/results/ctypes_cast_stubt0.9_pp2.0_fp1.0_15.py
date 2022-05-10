import ctypes
ctypes.cast(s, ctypes.c_void_p).value

# `s` is deleted and memory address is re-assigned
s = b"Hello, world!"
ctypes.cast(s, ctypes.c_void_p).value
</code>
What does "|None" mean in that first call, and what can I do to get around the problem?


A:

<code>|None</code> means <code>ctypes.cast(None, ctypes.c_void_p).value</code> which is <code>0</code> (or <code>0x00</code> if you're looking at the output of <code>hex(...)</code>).
<code>&gt;&gt;&gt; ctypes.cast(None, ctypes.c_void_p).value
0
</code>

