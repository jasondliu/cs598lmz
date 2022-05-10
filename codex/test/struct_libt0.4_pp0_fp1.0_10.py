import _struct

def _as_bytes(x):
    if isinstance(x, bytes):
        return x
    elif isinstance(x, str):
        return x.encode('latin1')
    elif isinstance(x, bytearray):
        return bytes(x)
    elif isinstance(x, memoryview):
        return x.tobytes()
    else:
        raise TypeError("Can't convert %s to bytes" % type(x))

def _pack_int(integer, size, le):
    """Pack a integer to bytes"""
    s = _struct.Struct(le + _struct.calcsize(str(size) + 'i'))
    return s.pack(integer)

def _unpack_int(data, size, le):
    """Unpack a integer from bytes"""
    s = _struct.Struct(le + _struct.calcsize(str(size) + 'i'))
    return s.unpack(data)

