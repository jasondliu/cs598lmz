import _struct
# Test _struct.Struct.unpack and _struct.Struct.pack

def unpack(fmt, data):
    return _struct.Struct(fmt).unpack(data)

def pack(fmt, *data):
    return _struct.Struct(fmt).pack(*data)

# Formats
fmt = 'cbhilfdsp'

# Data
data = (
    b'A',
    ord('\x00'),
    ord('\x01'),
    1,
    1,
    1.0,
    1.0,
    b'12345678',
    b'12345678901234567890',
)

# Test packing
packed = pack(fmt, *data)
if packed != b'A\x00\x01\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf0?\x00\x00\x00\x00\x00\x00@\x00\x00\x00
