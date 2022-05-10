from _struct import Struct
s = Struct.__new__(Struct)  # new struct class
s.format = '>lhhl'  # big-endian long, short, short, long
s.size = s.calcsize(s.format)
</code>
This is a bit more elegant than <code>struct.Struct('&gt;lhhl')</code> in that it can be reused, and you can get at the format string and the size without having to copy them.
<code>&gt;&gt;&gt; s.size
12
&gt;&gt;&gt; s.format
'&gt;lhhl'
</code>

