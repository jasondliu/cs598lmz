import _struct
# Test _struct.Struct.pack()

# Test pack with all the standard integer formats

for code in 'bBhHiIlLqQ':
    s = _struct.Struct(code)
    got = s.pack(1)
    expected = code + '\x01'
    if got != expected:
        print '%s.pack(1) == %r, expected %r' % (repr(s), got, expected)

# Test pack with size and alignment

for code, size, alignment in [('x', 1, 1),
                              ('c', 1, 1),
                              ('b', 1, 1),
                              ('b', 1, 2),
                              ('b', 1, 4),
                              ('b', 1, 8),
                              ('b', 2, 1),
                              ('b', 2, 2),
                              ('b', 2, 4),
                              ('b', 2, 8),
                              ('b', 4, 1),
                              ('b', 4, 2),
                              ('b', 4, 4),
                              ('b', 4, 8),
                
