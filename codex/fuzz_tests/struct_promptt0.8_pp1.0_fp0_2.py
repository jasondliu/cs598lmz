import _struct
# Test _struct.Struct.

AlignType = _struct.Struct(">h")
a = list(range(1, 100, 2))
print(a)
b = _struct.pack(">100h", *a)
print(AlignType.size)
print(AlignType.pack(3))
print(AlignType.unpack(b[:2]))
print(AlignType.unpack(b[2:4]))

# Test _struct.calcsize.
print(_struct.calcsize("100h"))
print(_struct.calcsize("100H"))
print(_struct.calcsize("100l"))
print(_struct.calcsize("100L"))
print(_struct.calcsize("100q"))
print(_struct.calcsize("100Q"))

# Test _struct.pack.
print(_struct.pack("100h", *a))
print(_struct.pack("100H", *a))
print(_struct.pack(">100l", *a))
print(_struct.pack(">100L", *a))
print(_struct.pack(">100
