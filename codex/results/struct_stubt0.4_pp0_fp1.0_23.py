from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.unpack(b'\x00\x00\x00\x01')
</code>
But I don't understand how this is possible.  I thought that <code>Struct</code>'s constructor was <code>Struct.__init__</code>, and that the <code>__new__</code> method was only called when you do <code>Struct()</code>.  But here, the <code>__new__</code> method seems to be called when you do <code>Struct.__new__(Struct)</code>.  Why does this work?


A:

<code>Struct</code> is a metaclass, and <code>Struct.__new__</code> is called when you call <code>Struct.__new__(Struct)</code> because it is the metaclass's <code>__new__</code> method.
When you call <code>Struct</code>, you are calling the metaclass's <code>__call__</code> method, which is not the same as the <code>__new__</code> method.
