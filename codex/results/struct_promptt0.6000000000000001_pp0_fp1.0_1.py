import _struct
# Test _struct.Struct class

def test_struct(typecode, size, alignment):
    if verbose:
        print('%r: size=%d, alignment=%d' % (typecode, size, alignment))
    s = _struct.Struct(typecode)
    assert s.size == size, 'expected size %d, got %d' % (size, s.size)
    assert s.alignment == alignment, 'expected alignment %d, got %d' % (alignment, s.alignment)
    assert s.format == typecode, 'expected format %r, got %r' % (typecode, s.format)
    if verbose:
        print('    pack:', end=' ')
    args = []
    for i in range(s.size):
        args.append(i)
        if verbose:
            print(i, end=' ')
    if verbose:
        print()
    packed = s.pack(*args)
    if verbose:
        print('   pack:', repr(packed))
    unpacked = s.unpack(packed)
    if
