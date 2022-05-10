import _struct
# Test _struct.Struct.format_size()

def test(fmt, expected):
    s = _struct.Struct(fmt)
    actual = s.format_size()
    if actual != expected:
        print('error in format %r: expected %d, got %d' % (fmt, expected, actual))

test('x', 1)
test('b', 1)
test('h', 2)
test('i', 4)
test('l', 4)
test('q', 8)
test('P', _struct.calcsize('P'))
test('s', 1)
test('p', _struct.calcsize('P'))
test('f', 4)
test('d', 8)

test('xx', 2)
test('bb', 2)
test('hh', 4)
test('ii', 8)
test('ll', 8)
test('qq', 16)
test('PP', 2 * _struct.calcsize('P'))
test('ss', 2)
test('pp', 2 * _struct.calcsize('P'))
test('ff', 8)
