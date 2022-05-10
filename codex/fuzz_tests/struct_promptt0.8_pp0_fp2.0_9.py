import _struct
# Test _struct.Struct.
_struct.Struct(b'i').pack(1)
# Test unaligned packing.
assert _struct.Struct(b'I').pack(1) == b'\x01\x00\x00\x00'

# Test for issue #2830.
s = b'0\0'
assert struct.pack('!h', 0) == s
assert struct.unpack('!h', s) == (0,)

print("passed all tests..")
