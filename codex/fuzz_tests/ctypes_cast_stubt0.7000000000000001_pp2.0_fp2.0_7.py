import ctypes
ctypes.cast(ctypes.c_void_p(0), ctypes.POINTER(ctypes.c_int16))
</code>
So this seems to be a bug in the ctypes module.
Update:
I reported the bug to the python bug tracker:
http://bugs.python.org/issue17207


A:

You can use the <code>from_address()</code> method of <code>ctypes</code> to create a pointer from an address:
<code>&gt;&gt;&gt; import ctypes
&gt;&gt;&gt; p = ctypes.c_int16.from_address(0)
&gt;&gt;&gt; p
c_short(0)
&gt;&gt;&gt; 
&gt;&gt;&gt; ctypes.cast(p, ctypes.c_char_p)
c_char_p(0)
&gt;&gt;&gt; 
&gt;&gt;&gt; ctypes.cast(p, ctypes.c_char_p).value
'\x
