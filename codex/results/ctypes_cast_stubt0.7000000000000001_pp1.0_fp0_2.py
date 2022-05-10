import ctypes
ctypes.cast(data, ctypes.POINTER(data_type))
</code>
and this works as expected, but I don't really understand what I'm doing, and would like to do it without using ctypes.  I've tried this (and other variants):
<code>ctypes.addressof(ctypes.pointer(data))
</code>
but it doesn't work.
Can I do this without using ctypes?  If so, how?


A:

<code>&gt;&gt;&gt; d=data_type()
&gt;&gt;&gt; d
&lt;__main__.data_type object at 0x00C8D930&gt;
&gt;&gt;&gt; p=ctypes.pointer(d)
&gt;&gt;&gt; p
&lt;ctypes.LP_data_type object at 0x00C8D9A0&gt;
&gt;&gt;&gt; p.contents
&lt;__main__.data_type object at 0x00C8D930&gt;
&gt;
