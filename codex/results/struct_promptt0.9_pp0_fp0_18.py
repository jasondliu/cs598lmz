import _struct
# Test _struct.Struct()'s pack()/unpack()
for fmt in ['b', 'c', 'u', 'h', 'H', 'i', 'I', 'l', 'L', 'q', 'Q', 'f', 'd']:
    tests = 0
    try:
        s = _struct.Struct(fmt)
        tests += 1
        s.pack(0)
    except TypeError:
        pass
    for n in range(1, 9):
        try:
            s = _struct.Struct(fmt * n)
            tests += 1
            s.pack(*[0] * n)
        except TypeError:
            pass
    if tests == 0:
        raise TestFailed("_struct.Struct(%r*n).pack() doesn't take n arguments"
                         % fmt)
# Reference tests
expect = ('\x12\x34\x56\x78\x9a\xbc\xde\xff'
          '\x00\x00\x00\x00\x00\x00\xac\x44'
          '\x00
