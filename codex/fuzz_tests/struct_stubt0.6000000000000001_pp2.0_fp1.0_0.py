from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.unpack_from(b'0000')
Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
TypeError: unpack_from() argument 1 must be bytes, not str
</code>
How can I pass a string to <code>unpack_from</code>?


A:

You need to use <code>struct.unpack_from(s, buffer, offset=0)</code>
<code>&gt;&gt;&gt; import struct
&gt;&gt;&gt; s = struct.Struct('i')
&gt;&gt;&gt; s.unpack_from(b'0000')
Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
TypeError: unpack_from() argument 1 must be bytes, not str
&gt;&gt;&gt; s.unpack_from(b'0000', 0)
(
