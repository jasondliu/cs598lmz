import _struct
# Test _struct.Struct, _struct.unpack_from(), _struct.pack_into(), and
# _struct.calcsize() with format string "=ii" (native, native).
# In this case struct.calcsize() should return 8.
print _struct.calcsize("=ii"), 8
a = _struct.pack_into("=ii", buffer(range(8)), 0, 100, 200)
print type(a), a
# The following raises a ValueError (the buffer is too small).
#a = _struct.pack_into("=ii", buffer(range(6)), 0, 100, 200)
#print type(a), a
print _struct.unpack_from("=ii", buffer(range(8)), 0), (0, 100)
# The following raises a ValueError (the buffer is too small).
#print _struct.unpack_from("=ii", buffer(range(6)), 0)
s = _struct.Struct("=ii")
print s.size, 8
print s.pack(100, 200), (0, 100)
print s.unpack(buffer(range(8))
