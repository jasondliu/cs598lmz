from _struct import Struct
s = Struct.__new__(Struct)
s.__init__("i")
s.unpack(b'i')
</code>
after the last line, the <code>s</code> variable is replaced with an integer: <code>1</code>. This is not what I want. The documentation says:
<blockquote>
<p>unpack(buffer)<br/>
  Unpack the buffer according to the format string format. The result is a tuple even if it contains exactly one item. The buffer’s size in bytes must match the size required by the format, as reflected by calcsize().</p>
</blockquote>
I understand that the result is a tuple, but what I don't understand, where does the <code>1</code> come from?


A:

<code>1</code> is the length of the buffer.

<code>&gt;&gt;&gt; s = Struct.__new__(Struct)
&gt;&gt;&gt; s.__init__("i")
&gt;&gt;&gt; s.unpack(b'i')
(1,)
&gt
