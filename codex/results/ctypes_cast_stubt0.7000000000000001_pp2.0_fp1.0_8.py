import ctypes
ctypes.cast(array_ulong, ctypes.POINTER(ctypes.c_ulong))
</code>


A:

You can use <code>ctypes.POINTER</code> to cast the pointer.
<code>&gt;&gt;&gt; import ctypes
&gt;&gt;&gt; array_ulong = (ctypes.c_ulong * 2)()
&gt;&gt;&gt; ctypes.POINTER(ctypes.c_ulong).from_buffer(array_ulong)
&lt;__main__.LP_c_ulong object at 0x7f7e4d64e0e0&gt;
</code>

