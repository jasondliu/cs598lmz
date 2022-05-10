import _struct
# Test _struct.Struct
format1 = 'hhl'
s = _struct.Struct(format1)
s.size
s.pack(1, 2, 3)
s.pack_into('hhl', buffer(bytearray(20)), 5, 1, 2, 3)
s.unpack(buffer(bytearray(s.pack(1, 2, 3)))), s.unpack_from(buffer(bytearray(20)), 5)
# Test struct.pack_iter
import struct
format1 = 'hhl'
struct.pack_iter('12' + format1, [1, 2, 3])
it = iter(struct.pack_iter('12' + format1, [1, 2, 3]))
list(it)
struct.Struct('12' + format1).size
iter(struct.pack_iter('12' + format1, [1, 2, 3])).next()
struct.Struct('12I').size
list(iter(struct.pack_iter('12' + format1, [1, 2, 3])))
iter(struct.pack_iter('12' + format
