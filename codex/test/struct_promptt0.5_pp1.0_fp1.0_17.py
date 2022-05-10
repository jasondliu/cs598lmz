import _struct
# Test _struct.Struct.

def test(format, expected):
    s = _struct.Struct(format)
    print(repr(s.format), s.size, repr(s.pack(expected)))
    print(s.unpack(s.pack(expected)))
    print(s.unpack_from(s.pack(expected), 0))
    print(s.unpack_from(s.pack(expected), 0), s.unpack_from(s.pack(expected), 0))
    print(s.unpack(s.pack_into(bytearray(), 0, expected)))
    print(s.unpack_from(s.pack_into(bytearray(), 0, expected), 0))
    print(s.unpack_from(s.pack_into(bytearray(), 0, expected), 0),
          s.unpack_from(s.pack_into(bytearray(), 0, expected), 0))

# Simple examples
test("ccc", (b"1", b"2", b"3"))
test("ccc", (49, 50, 51))

