from _struct import Struct
s = Struct.__new__(Struct)
s.__init__("H", "")
s.unpack("")
</code>
This gives the error:
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
error: unpack requires a string argument of length 2
</code>
Here's how to reproduce it another way:
<code>&gt;&gt;&gt; from _struct import Struct
&gt;&gt;&gt; Struct("H").unpack("")
Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
error: unpack requires a string argument of length 2
</code>
Any ideas what's going on?

