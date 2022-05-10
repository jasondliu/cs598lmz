from _struct import Struct
s = Struct.__new__(Struct)
s.format = "<3s3sHH"
s.size = 14
</code>
The documentation for the <code>struct</code> module states:
<blockquote>
<p>The Struct module can interpret these format strings (or any compatible format strings written by hand).</p>
</blockquote>
Why can't <code>_struct</code> interpret these format strings?


A:

After experimenting with this, it seems that <code>_struct</code> can not interpret the format strings. <code>_struct</code> only uses the <code>struct</code> format strings to infer its own format strings, and after that, it goes its own way.
For example, the <code>&lt;</code> indicates native byte order. But <code>_struct</code> does not have the concept of byte order.
<code>&gt;&gt;&gt; import _struct
&gt;&gt;&gt; _struct.pack("&lt;3s3sHH", b"foo", b"bar", 42, 3)
b'\x00\x00\x
