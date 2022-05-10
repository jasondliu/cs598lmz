import _struct
# Test _struct.Struct and all endians.
#
# This test is not really portable, but it's useful in checking that _struct
# is working properly.  It could be expanded to test more of the function.
print('Test _struct.Struct methods.')

for endian in '<>!=':
    print('Endian', endian)
    s = _struct.Struct(endian + 'l')
    print('Size', s.size)
    assert s.size == 4
    print('Format', s.format)
    assert s.format == endian + 'l'
    print('Align', s.align)
    assert s.align == '\x04'
    print('Packs', s.pack(0x1234))
    assert s.pack(0x1234) == eval('b"' + endian + '\x34\x12\x00\x00"')
    print('Packs', s.pack(0x12345678))
