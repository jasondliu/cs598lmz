import _struct
# Test _struct.Struct
try:
    _struct.Struct
except AttributeError:
    print("SKIP")
    raise SystemExit

s = _struct.Struct("<i")

# test pack/unpack
print(s.pack(12345))
print(s.unpack(s.pack(12345)))

# test size
print(s.size)

# test pack_into/unpack_from
buf = bytearray(s.size)
s.pack_into(buf, 0, 12345)
print(buf)
print(s.unpack_from(buf, 0))
