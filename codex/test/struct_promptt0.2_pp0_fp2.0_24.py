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
test('B', 1)
test('H', 2)
test('I', 4)
test('L', 4)
test('Q', 8)
test('f', 4)
test('d', 8)
test('s', 1)
test('p', 1)
test('P', 4)

test('cx', 2)
test('cxB', 3)
test('cxBH', 5)
test('cxBHI', 9)
test('cxBHIL', 13)
test('cxBHILQ', 21)
