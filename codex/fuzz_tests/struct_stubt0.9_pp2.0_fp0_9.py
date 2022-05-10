from _struct import Struct
s = Struct.__new__(Struct)
s.format('&lt;I')
</code>
Output:
<code>&gt;&gt;&gt; s.format('&lt;I')
&lt;class '_struct.Struct'&gt;
&gt;&gt;&gt; s.unpack_from('\x00\x00\x00\x04', 0)
(4L,)
&gt;&gt;&gt; s.unpack_from('\x04\x00\x00\x00', 0)
(4L,)
</code>

