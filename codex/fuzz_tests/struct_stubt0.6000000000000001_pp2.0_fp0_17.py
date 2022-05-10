from _struct import Struct
s = Struct.__new__(Struct)
s.__init__("@", "")
len(s.pack(0))
</code>
Which gives me a segfault.
Is there a better way to get the size of a struct?


A:

You can use <code>struct.calcsize</code> to get the size of the struct.
<code>&gt;&gt;&gt; import struct
&gt;&gt;&gt; struct.calcsize("@")
&gt;&gt;&gt; struct.calcsize("@i")
8
&gt;&gt;&gt; struct.calcsize("@ii")
16
&gt;&gt;&gt; struct.calcsize("@iii")
24
&gt;&gt;&gt; struct.calcsize("@iiii")
32
</code>

