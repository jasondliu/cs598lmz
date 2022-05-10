import _struct

# http://docs.python.org/2/library/struct.html
# The following specifiers are used for packing unsigned integers:
#   = B
#   > H L P
#   I Q &
# > = big endian, < = little endian
_struct_unpack = {
    'u1': ('B', 0),
    'u2be': ('>H', 0),
    'u2le': ('<H', 0),
    'u4be': ('>L', 0),
    'u4le': ('<L', 0),
    'u8be': ('>Q', 0),
    'u8le': ('<Q', 0),
    'u8ne': ('Q', 0),
}

def unpack(fmt, data):  # _struct_unpack
    fmt, offset = _struct_unpack[fmt]
    return _struct.unpack(fmt, data)[offset]

def construct(fmt, field_names):
    fmt = [_struct_unpack[fmt][0]] + field_names

