from _struct import Struct
s = Struct.__new__(Struct)
s.size = 1
s.format = 'H'
</code>
Or, for a more complete example:
<code>&gt;&gt;&gt; from _struct import Struct
&gt;&gt;&gt; s = Struct.__new__(Struct)
&gt;&gt;&gt; s.size = 1
&gt;&gt;&gt; s.format = 'H'
&gt;&gt;&gt; s.unpack(b'\x01\x02')
(258,)
</code>

