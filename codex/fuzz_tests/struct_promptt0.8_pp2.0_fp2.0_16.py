import _struct
# Test _struct.Struct.
s = _struct.Struct(b'<i')
buf = bytes(s.size)
s.pack_into(buf, 0, 2)
print(s.unpack_from(buf, 0))

# Test _struct.Struct.get_size()
print(s.get_size())

# Test _struct.Struct.get_format()
print(s.get_format())

# Test _struct.calc_buflen()
print(_struct.calc_buflen(b'<i', 2))

# Test _struct.Struct.pack_into() with overflowing data
buf = bytes(2*s.size)
s.pack_into(buf, 0, 2)
with self_expect_stderr(stderr):
    s.pack_into(buf, 0, 2**100)
