from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('16s')
s.unpack(b'Hello\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')

# outputs:
# b'Hello'
</code>
So I'm pretty sure this only happens for <code>struct</code> objects created by calling <code>struct.Struct</code> (or the internal <code>_struct.Struct</code>). I'm not sure why that would be.

