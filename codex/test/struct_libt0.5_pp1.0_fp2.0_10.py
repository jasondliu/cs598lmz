import _struct

def _pack_float(f, size):
    if size == 4:
        return _struct.pack('f', f)
    elif size == 8:
        return _struct.pack('d', f)
    else:
        raise TypeError("size must be 4 or 8")

def _unpack_float(s, size):
    if size == 4:
        return _struct.unpack('f', s)[0]
    elif size == 8:
        return _struct.unpack('d', s)[0]
    else:
        raise TypeError("size must be 4 or 8")

def _pack_float_le(f, size):
    if size == 4:
        return _struct.pack('<f', f)
    elif size == 8:
        return _struct.pack('<d', f)
    else:
        raise TypeError("size must be 4 or 8")

def _unpack_float_le(s, size):
    if size == 4:
        return _struct.unpack('<f', s)[0]
   
