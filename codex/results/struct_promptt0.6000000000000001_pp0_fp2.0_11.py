import _struct
# Test _struct.Struct with all native byte orders.
for order in '@=<>!':
    s = _struct.Struct(order + 'h')
    x = s.unpack(b'\x00\x01')[0]
    if x != 1:
        print('error in', order, x)
# Test _struct.Struct with native size and alignment.
for code in 'bBhHiIlLqQfd':
    fmt = '@' + code * 2
    s = _struct.Struct(fmt)
    size = s.size
    alignment = s.alignment
    if code in 'bB':
        expect_size = 2
        expect_alignment = 1
    elif code in 'hHiI':
        expect_size = 4
        expect_alignment = 2
    elif code in 'lLqQ':
        expect_size = 8
        expect_alignment = 4
    elif code == 'f':
        expect_size = 4
        expect_alignment = 4
    elif code == 'd':
        expect_size = 8
        expect
