import _struct
# Test _struct.Struct
test_struct = _struct.Struct(b"i5s")
test_struct.size
test_struct.pack(1, b"hello")
test_struct.pack_into(bytearray(test_struct.size), 0, 1, b"hello")
test_struct.unpack(test_struct.pack(1, b"hello"))
test_struct.unpack_from(test_struct.pack(1, b"hello"), 0)

# Test _struct.calcsize
_struct.calcsize(b"i5s")

# Test _struct.error
try:
    test_struct.pack()
except _struct.error as e:
    print(e)

# Test module level _struct.pack
_struct.pack(b"i5s", 1, b"hello")
# _struct.pack_into
_struct.pack_into(bytearray(test_struct.size), 0, b"i5s", 1, b"hello")
# _struct.unpack
_struct.unpack(b"i5s", test_
