from _struct import Struct
s = Struct.__new__(Struct)
s.format = "I"
s.size = struct.calcsize(s)
print(s.size)
print(s.format)
</code>
The output is:
<code>4
'I'
4
I
</code>
Python 3.x
<code>from _struct import Struct
s = Struct.__new__(Struct)
s.format = "I"
print(s.size)
print(s.format)
</code>
The output is:
<code>&lt;property object at 0x108401f28&gt;
I
</code>
Are we supposed to always call <code>struct.calcsize()</code> when we write the code? If not, what is the <code>struct.calcsize()</code> for?


A:

<code>Struct.size</code> is not a constant, it is a property:
<code>&gt;&gt;&gt; Struct.size == Struct.size
False
</code>
The value is looked up on demand:
<code>&gt;
