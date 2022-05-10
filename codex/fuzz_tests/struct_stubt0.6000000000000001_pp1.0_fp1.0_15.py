from _struct import Struct
s = Struct.__new__(Struct)
s.__setattr__('_fmt', '12s f')
s.__setattr__('size', s.size)
s.__setattr__('pack', s.pack)
s.__setattr__('unpack', s.unpack)
s.__setattr__('format', s.format)
</code>
However, when I try to use the module from the command line, I can't access the attributes of s:
<code>&gt;&gt;&gt; import struct
&gt;&gt;&gt; s = struct.Struct.__new__(struct.Struct)
&gt;&gt;&gt; s.__setattr__('_fmt', '12s f')
&gt;&gt;&gt; s.__setattr__('size', s.size)
&gt;&gt;&gt; s.__setattr__('pack', s.pack)
&gt;&gt;&gt; s.__setattr__('unpack', s.unpack)
&gt;&gt;&gt; s.__setattr__
