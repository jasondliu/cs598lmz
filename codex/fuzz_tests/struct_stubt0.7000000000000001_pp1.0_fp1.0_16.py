from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('bbbb')
s.unpack_from(b'\x01\x02\x03\x04')
</code>
I'm using Python 3.6, but I don't think that should matter.


A:

I'm not sure if this is a bug or not, but it looks like you are passing the format string in the wrong way. If you use the following code, it works just fine.
<code>&gt;&gt;&gt; from _struct import Struct
&gt;&gt;&gt; s = Struct('bbbb')
&gt;&gt;&gt; s.unpack_from(b'\x01\x02\x03\x04')
(1, 2, 3, 4)
</code>

