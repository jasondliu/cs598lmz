import _struct
# Test _struct.Struct.__init__ and _struct.Struct.format

def test(fmt, expected):
    print fmt, expected
    s = _struct.Struct(fmt)
    got = s.format
    if got != expected:
        raise RuntimeError, '%r != %r' % (got, expected)

test('', '')
test('b', 'b')
test('B', 'B')
test('h', 'h')
test('H', 'H')
test('i', 'i')
test('I', 'I')
test('l', 'l')
test('L', 'L')
test('q', 'q')
test('Q', 'Q')
test('f', 'f')
test('d', 'd')
test('s', 's')
test('p', 's')
test('P', 's')
test('c', 'c')
test('c', 'c')
test('?', '?')

test('bb', 'bb')
test('bbb', 'bbb')
test('bbbb', 'bbbb')
test('bb
