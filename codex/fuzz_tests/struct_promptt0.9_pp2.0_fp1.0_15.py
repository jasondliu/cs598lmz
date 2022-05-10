import _struct
# Test _struct.Struct methods

for codes in ('bBcCsSlLiIf', 'xd'):
    fmt = ' ' + codes
    sz = _struct.calcsize(fmt)
    for i in range(sz):
        data = _struct.pack(fmt, *range(1, i + 2))
        for offset in range(sz):
            for size in range(1, sz - offset + 1):
                value = _struct.unpack_from(fmt, data, offset)[0]
                s = _struct.Struct(codes)
                buf = memoryview(data)
                sl = buf[offset:offset + size]
                got = s.unpack_from(sl)
                err = "for format code %s, size %d, at offset %d: got %r, expected %r" \
                      % (codes, size, offset, got, value)
                assert got == value, err
                got = s.unpack_from(sl.tobytes())
                err = "for format code %s, size %d, at offset %d: got %r
