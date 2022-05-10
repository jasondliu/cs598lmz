import _struct
# Test _struct.Struct.

# Test packing and unpacking of basic types.

s = _struct.Struct("bBhHiIqQfd")

# Test pack.

bs = s.pack(1, 2, 3, 4, 5, 6, 7, 8, 9.0, 10.0)
print(repr(bs))
print(s.size)
print(len(bs))

# Test unpack.

print(s.unpack(bs))

# Test unpack with buffer.
print(s.unpack_from(bs, 4))

# Test the native version.

try:
    s = _struct.Struct("@bBhHiIqQfd")

    # Test pack.

    bs = s.pack(1, 2, 3, 4, 5, 6, 7, 8, 9.0, 10.0)
    print(repr(bs))
    print(s.size)
    print(len(bs))

    # Test unpack.

    print(s.unpack(bs))

    # Test unpack with buffer.
   
