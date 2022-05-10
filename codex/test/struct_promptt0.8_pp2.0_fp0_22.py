import _struct
# Test _struct.Struct
basic_format = "iif6s"
# Standard sizes
_struct.calcsize(basic_format)

# !r format
_struct.Struct(basic_format)

# !s format
_struct.Struct(basic_format).format

# !S format
_struct.Struct(basic_format).format_size

# !t format
_struct.Struct(basic_format).alignment

# bad format
try:
    _struct.calcsize("1234")
except struct.error:
    print("no size known for type")

# pack
_struct.pack(basic_format, 1, 2, 3.1, b'abc')

# unpack
_struct.unpack(basic_format, b'\x01\x00\x00\x00\x02\x00\x00\x00\xcd\xcc\xcc\xcc\xcc\xcc\xcc')

# in/out buffers
