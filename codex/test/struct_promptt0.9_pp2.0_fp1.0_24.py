import _struct
# Test _struct.Struct on an endianness that is used by a real platform.
# On this platform, the host byte order is little-endian.
struct1 = _struct.Struct('=BhLi')
struct2 = _struct.Struct('<BhLi')
struct3 = _struct.Struct('>BhLi')
struct4 = _struct.Struct('@BhLi')
try:
    buf1 = struct1.pack(1, -2, 3, 4)
except RuntimeError:
    print('platform does not support all formats')
    import sys
    sys.exit(1)
buf2 = struct2.pack(1, -2, 3, 4)
buf3 = struct3.pack(1, -2, 3, 4)
buf4 = struct4.pack(1, -2, 3, 4)
print(buf1)
print(buf2)
print(buf3)
print(buf4)
print('unpack(buf1) =>', struct1.unpack(buf1))
print('unpack(buf2) =>', struct1.unpack(buf2))
