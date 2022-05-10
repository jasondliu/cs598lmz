import _struct
# Test _struct.Struct.

def test(fmt, expected):
    s = _struct.Struct(fmt)
    got = s.size
    if got != expected:
        print('error in _struct.Struct(%r).size: expected %d, got %d' %
              (fmt, expected, got))

test('x', 1)
test('c', 1)
test('b', 1)
test('B', 1)
test('h', 2)
test('H', 2)
test('i', 4)
test('I', 4)
test('l', 4)
test('L', 4)
test('q', 8)
test('Q', 8)
test('f', 4)
test('d', 8)
test('s', 1)
test('p', 1)
test('P', 1)

test('xi', 5)
test('cx', 2)
test('bx', 2)
test('Bx', 2)
test('hx', 3)
test('Hx', 3)
test('ix', 6)
test('Ix', 6)

