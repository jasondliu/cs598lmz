import _struct
# Test _struct.Struct
try:
    s = _struct.Struct('i')
except _struct.error:
    pass # handled by test_struct
else:
    eq(s.size, 4)
    eq(s.pack(12345), '\x39\x30\x00\x00')
    eq(s.unpack('\x39\x30\x00\x00'), (12345,))
    raises(struct.error, s.pack, 12345, 67890)
    raises(TypeError, s.unpack, '\x39\x30\x00\x00', 67890)

# Test _struct.calcsize
try:
    n = _struct.calcsize('i')
except _struct.error:
    pass # handled by test_struct
else:
    eq(n, 4)

# Test _struct.pack
try:
    s = _struct.pack('i', 12345)
except _struct.error:
    pass # handled by test_struct
else:
    eq(s, '\x39\x30\x
