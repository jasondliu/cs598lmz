import _struct
# Test _struct.Struct.unpack() on binary data with a format that is
# smaller than the size of the binary data
for i in range(1, 100):
    s = _struct.Struct(bytes(i))
    try:
        s.unpack(bytes(100))
    except Exception:
        pass
# Test _struct.Struct.unpack_from() on binary data with a format that is
# smaller than the size of the binary data
for i in range(1, 100):
    s = _struct.Struct(bytes(i))
    try:
        s.unpack_from(bytes(100))
    except Exception:
        pass
