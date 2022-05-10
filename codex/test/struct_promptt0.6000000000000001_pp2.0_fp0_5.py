import _struct
# Test _struct.Struct.format_size() with byte order, signedness, and alignment.

for byteorder in ['@', '=', '<', '>', '!', '^', '&', '*']:
    for format in ['x', 'b', 'B', 'h', 'H', 'i', 'I', 'l', 'L', 'q', 'Q', 'f',
       'd']:
        for alignment in [0, 1, 2, 4, 8]:
            fmt = byteorder + format
            s = _struct.Struct(fmt)
            size = s.size
            if alignment:
                fmt = fmt + str(alignment)
            size2 = s.format_size(fmt)
            if size != size2:
                print(fmt, size, size2)
