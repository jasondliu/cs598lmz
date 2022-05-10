from _struct import Struct
s = Struct.__new__(Struct)
s.size = 88
s.format = 'B b 8s d l d f 33s c'
s.pack_into(buf, 0, 1, 1, b'foobar  ', 3.14, -42, 3.14, 42.5, b'quuxxxxxxxxxxxxxxxxxxxxxxx', ord('a'))
</code>
rather than the more obvious
<code>s = Struct('B b 8s d l d f 33s c')
s.pack_into(buf, 0, 1, 1, b'foobar  ', 3.14, -42, 3.14, 42.5, b'quuxxxxxxxxxxxxxxxxxxxxxxx', ord('a'))
</code>
I expect that this is to avoid a recursive import, or something like that, but I don't really get it.
Can someone explain why code like this is common, and what it means?


A:

Let's look at the source code for <code>Struct</code>. (I'm using CPython 2.7 for this example, but this still applies for 3.x.)
Each <code>Struct</code> subclass has an attribute
