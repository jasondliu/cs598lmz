import _struct
# Test _struct.Struct with too many arguments
for fmt in [('b', 'B', 'h', 'H', 'i', 'I', 'l', 'L', 'f', 'd', 'c'):
    s = _struct.Struct(fmt)
    try:
        s.pack(1, 2)
    except Exception:
        pass
    else:
        print('expected error')
    try:
        s.pack_into(buf, 0, 1, 2)
    except Exception:
        pass
    else:
        print('expected error')
    try:
        s.unpack(buf)
    except Exception:
        pass
    else:
        print('expected error')
    try:
        s.unpack_from(buf, 0)
    except Exception:
        pass
    else:
        print('expected error')
# Test _struct.Struct with too few arguments
for fmt in [('b', 'B', 'h', 'H', 'i', 'I', 'l', 'L', 'f', 'd', 'c'):
    s = _struct.Struct(fmt
