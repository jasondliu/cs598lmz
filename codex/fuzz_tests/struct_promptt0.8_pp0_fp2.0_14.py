import _struct
# Test _struct.Struct("i").pack()
# with big endian (network byte order)
# and little endian (native byte order)
# format for int
for t, v in [("<i", 1), (">i", 1)]:
    print t
    s = _struct.Struct(t)
    print s.pack(v)
    print s.unpack(s.pack(v))
