import ctypes
ctypes.cast(buf, ctypes.POINTER(ctypes.c_ubyte))
</code>
From here, you can assign a Python <code>bytes</code> literal: <code>foo = b'abcdef'</code>, and the Python <code>foo</code> variable will be used to place the string literal in memory. You can even get the address of the string literal itself using <code>id()</code> and pass that to the IDAPython <code>buf</code> variable:
<code>&gt;&gt;&gt; import ctypes
&gt;&gt;&gt; foo = b'abc'
&gt;&gt;&gt; buf = idaapi.put_many_bytes(id(foo), len(foo))    # assume this is already the case
&gt;&gt;&gt; ctypes.cast(buf, ctypes.POINTER(ctypes.c_ubyte)).contents.value
97
&gt;&gt;&gt; id(foo) == id(buf)
True
</code>
If this were a simple matter, you could do
