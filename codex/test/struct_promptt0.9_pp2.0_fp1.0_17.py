import _struct
# Test _struct.Struct implementation
print('sizeof(int) = %d' % _struct.calcsize('i'))
print('sizeof(int) = %d' % _struct.calcsize('!i'))
# Test _struct.unpack and _struct.pack
s = _struct.Struct(' !ii ')
packed = s.pack(1, 2)
print('packed size = %d' % len(packed))
print('%s = 1 and 2' % s.unpack(packed))
# Test _struct.pack_into and _struct.unpack_from
# Extra space is used to fill out the buf
buffer = array.array('b', b'\x00' * s.size)
print(type(buffer))
s.pack_into(buffer, 0, 42, 42)
print(type(buffer))
print(buffer)
print(s.unpack_from(buffer, 0))
 
