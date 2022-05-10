from _struct import Struct
s = Struct.__new__(Struct)
s.format = b'I'
s.size = 4
s.pack = Struct.__dict__['pack']
s.unpack = Struct.__dict__['unpack']
s.pack(1)
</code>
I suspect that this is because the format string is being passed to C code that uses a different buffer object implementation.
Is there a way to create a "struct" object that can be used with Python 3.2?
(It's OK if it's not exactly the same as the ones created by the <code>Struct</code> class.)


A:

You can use <code>struct.calcsize</code> and <code>struct.pack</code> to do the same as the <code>Struct</code> class.
<code>fmt1 = b'&lt;I'
size = struct.calcsize(fmt1)
data = struct.pack(fmt1, 1)

fmt2 = b'&lt;HH'
size = struct.calcsize(fmt2)
data = struct.pack(fmt2, 1, 2)

