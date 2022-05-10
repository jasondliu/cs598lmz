import _struct
# Test _struct.Struct.pack_into

def pack_into(msg, endian, fmt, buf):
    s = _struct.Struct('_' + endian + fmt)
    return str(s.pack_into(buf, 5, *msg))

def unpack_from(endian, fmt, buf, msg):
    s = _struct.Struct('_' + endian + fmt)
    s.unpack_from(buf, 5) == msg

b = buffer(range(50))
buf = pack_into((1, 2.0, 3.0+4.0j), 'html', 'Bdh', b)
unpack_from('html', 'Bdh', buf, (1, 2.0, 3.0+4.0j))

buf = pack_into((1, 2.0, 3.0+4.0j), 'lhil', 'Bdh', b)
unpack_from('lhil', 'Bdh', buf, (1, 2.0, 3.0+4.0j))

buf = pack_into((1, 2.0, 3
