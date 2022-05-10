from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('hhl', bytearray(b'\x01\x00\x00\x00\x02\x00\x03\x00'), 0)
s.format_str = 'hhl'
s.size = struct.calcsize(s.format_str)
s.unpack_from(bytearray(b'\x01\x00\x00\x00\x02\x00\x03\x00'), 0)
</code>
This should be equivalent to the first, but instead I get the same error.
After some more digging, I found a couple more classes that are worth noting as well: <code>Struct</code>, <code>StructSequence</code>, <code>_clearcache</code>. These classes interact in different ways, which makes it difficult to figure out how to properly mock them.
The first, <code>Struct</code>, can be found in <code>_struct.py</code>. I think this is the class that we want to mock in the <code>struct</code> module. The second, <code>StructSequ
