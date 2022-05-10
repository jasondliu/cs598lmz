from _struct import Struct
s = Struct.__new__(Struct)
s.format = '2s f'
s.size = s.calcsize(s.format)
print s.size
</code>
EDIT:
For python 2.7
<code>&gt;&gt;&gt; from _struct import Struct
&gt;&gt;&gt; s = Struct.__new__(Struct)
&gt;&gt;&gt; s.format = '2s f'
&gt;&gt;&gt; s.size = s.calcsize(s.format)
&gt;&gt;&gt; print s.size
6
</code>

