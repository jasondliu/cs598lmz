import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int(1)

s = S()
print hex(id(s)), hex(id(s.x))

s.x = 2
print hex(id(s)), hex(id(s.x))
</code>
Both ids are the same. Why does that happen?


A:

Because it is just a pointer to an integer.
<code>&gt;&gt;&gt; id(s)
20502640
&gt;&gt;&gt; id(s.x)
20502640
&gt;&gt;&gt; s.contents
c_int(1)
&gt;&gt;&gt; id(s.contents)
20502640
&gt;&gt;&gt; s.x = 2
&gt;&gt;&gt; id(s.x)
20502640
&gt;&gt;&gt; id(s.contents)
20502640
</code>

