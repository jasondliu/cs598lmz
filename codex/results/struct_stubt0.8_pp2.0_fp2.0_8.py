from _struct import Struct
s = Struct.__new__(Struct)
print(s)
# &lt;class '_struct.Struct'&gt;
</code>
Although when I try to do the same for <code>collections.namedtuple</code> I get an error:
<code>&gt;&gt;&gt; from collections import namedtuple
&gt;&gt;&gt; nt = namedtuple.__new__(namedtuple)
Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
TypeError: Required argument 'typename' (pos 1) not found
</code>
What happened?


A:

The <code>namedtuple</code> function creates a factory method to make a <code>namedtuple</code> subclass. The <code>namedtuple.__new__()</code> method is not a constructor!
<code>from collections import namedtuple

nt = namedtuple('nt', 'x y z')

print(isinstance(nt, type))
# True
print(isinstance(
