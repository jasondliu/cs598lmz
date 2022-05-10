import _struct
# Test _struct.Struct for all combinations of the flags
# 0, _struct.LITTLE_ENDIAN, _struct.BIG_ENDIAN and _struct.NATIVE_ENDIAN.
# The latter two only have an effect on systems with more than one
# native byte order. For example big-endian and little-endian ARM systems.
#
# Without flags, the default is native byte order.
#
# We test all formats for packing a single value, unpacking one value,
# packing and unpacking a list and packing and unpacking a dict.
#
for endianness in (0, _struct.LITTLE_ENDIAN, _struct.BIG_ENDIAN, _struct.
    NATIVE_ENDIAN):
    print('-' * 30)
    print('endianness=', endianness)
    for format in ALL_FORMATS:
        print('format=', format)
        print('-' * 30)
        s = _struct.Struct(format)
        print(format, 'size=', s.size)
