import _struct
# Test _struct.Struct.__getitem__
class S(tuple):
    pass
def unpack_from(self, buffer, offset=0):
    if offset != 0 or buffer[0] != 'M':
        raise Exception
    return S((buffer[0],))
def pack_into(self, fmt, buffer, offset, *args):
    if fmt != 'M' or offset != 0 or buffer[0] != '@':
        raise Exception
    buffer[0] = args[0]
_struct.Struct.unpack_from = unpack_from
_struct.Struct.pack_into = pack_into
struct = _struct.Struct('M')
try:
    struct['M']
    raise Exception
except TypeError:
    pass

try:
    struct['MM']
    raise Exception
except TypeError:
    pass

try:
    struct['']
    raise Exception
except TypeError:
    pass

buffer = bytearray('@')
struct.pack_into(buffer, 1, 'M')
assert buffer == bytearray('@M')

