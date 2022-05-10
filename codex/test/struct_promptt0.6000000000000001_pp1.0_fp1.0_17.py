import _struct
# Test _struct.Struct.
s = _struct.Struct('hhl')
s.size
s.pack(1, 2, 3)
s.unpack(s.pack(1, 2, 3))
s.unpack_from(s.pack(1, 2, 3), 0)
s.unpack_from(s.pack(1, 2, 3), 1)
s.unpack_from(s.pack(1, 2, 3), 2)
# Test buffer interface.
s.pack_into(buffer('\0' * s.size), 0, 1, 2, 3)
s.unpack_from(buffer(s.pack(1, 2, 3)), 0)
s.unpack_from(buffer(s.pack(1, 2, 3)), 1)
s.unpack_from(buffer(s.pack(1, 2, 3)), 2)
# Test array interface.
import array
s.pack_into(array.array('c', '\0' * s.size), 0, 1, 2, 3)
