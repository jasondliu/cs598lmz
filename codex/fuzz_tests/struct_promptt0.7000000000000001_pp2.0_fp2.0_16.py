import _struct
# Test _struct.Struct

# s.pack(v1, v2, ...) method
args = [1, 2.3, 'abc']
s = _struct.Struct('hhh3s')
b = s.pack(*args)
print(repr(b))
print(s.unpack(b))

# s.pack_into(buffer, offset, v1, v2, ...) method
args = [1, 2.3, 'abc']
s = _struct.Struct('hhh3s')
b = bytearray(s.size)
s.pack_into(b, 0, *args)
print(repr(b))
print(s.unpack_from(b, 0))

# s.unpack(buffer) method
args = [1, 2.3, 'abc']
s = _struct.Struct('hhh3s')
b = s.pack(*args)
print(repr(b))
print(s.unpack(b))

# s.unpack_from(buffer, offset=0) method
args = [1, 2.3, 'abc']
