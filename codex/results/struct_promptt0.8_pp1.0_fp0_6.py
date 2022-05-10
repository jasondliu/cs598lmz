import _struct
# Test _struct.Struct over all possible formats

fmtstr = 'bBhHiIlLfdcspzP'

# little-endian
for fmt in fmtstr:
    lstruct = _struct.Struct(fmt)
    print('little-endian', fmt)

    # test padding bytes
    for offset in range(20):
        print('    ', offset)
        exp = _struct.pack(fmt, 1)
        exp = b'\0' * offset + exp
        if fmt in 'spz':
            exp = exp + b'\0'
        assert lstruct.size == len(exp) - offset
        if fmt == 'z':
            # z has variable size
            assert lstruct.pack('') == b'\0'
            assert lstruct.unpack(exp) == (b'',)
            assert lstruct.unpack(b'\0') == (b'',)
            assert lstruct.unpack(b'\0\0') == (b'\0',)
            exp = b'\0' * offset + b'x'
        else
