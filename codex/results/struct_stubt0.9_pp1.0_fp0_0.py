from _struct import Struct
s = Struct.__new__(Struct)

s.size = s.__sizeof__()

print(s.size)
</code>


A:

Last time I checked, this worked:
<code>&gt;&gt;&gt; from _struct import Struct
&gt;&gt;&gt; s = Struct.__new__(Struct)
&gt;&gt;&gt; s.size = s.format.__sizeof__()
&gt;&gt;&gt; s.size
8
</code>

