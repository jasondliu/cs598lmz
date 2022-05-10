import _struct
# Test _struct.Struct.validate_size
#
# Check the size of structs created is always compatible with the native
# alignment properties.
NATIVE_ENDIAN = _struct.unpack('=i', b'\x00\x00\x00\x01')[0] == 1
# Valid sizes
VALID_SIZES = {
    '=1x     ': (0, 1),
    '=14     ': (14, 14),
    '=15     ': (15, 16),
    '<1x     ': (0, 1),
    '<14     ': (14, 14),
    '<15     ': (15, 16),
    '>1x     ': (0, 1),
    '>14     ': (14, 14),
    '>15     ': (15, 16)}
