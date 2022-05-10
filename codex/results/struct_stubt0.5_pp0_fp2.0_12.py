from _struct import Struct
s = Struct.__new__(Struct)
s.__init__()
s.unpack_from(b'\x01\x02\x03\x04', 0)
</code>
I'm getting the error <code>TypeError: unpack_from() argument 1 must be string, not bytes</code>. 
Why is that, and how can I fix it?


A:

You're using the wrong type of <code>Struct</code>.  The <code>struct</code> module has two classes, <code>Struct</code> and <code>Struct.Struct</code>.  You want the latter.
<code>from _struct import Struct
s = Struct.__new__(Struct.Struct)
s.__init__()
s.unpack_from(b'\x01\x02\x03\x04', 0)
</code>

