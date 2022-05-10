import _struct
# Test _struct.Struct.format_size()

def test(fmt, expected):
    s = _struct.Struct(fmt)
    actual = s.format_size()
    if actual != expected:
        print('Error in', fmt)
        print('Expected', expected)
        print('Got', actual)

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
test('c', 1)

test('2x', 2)
test('2b', 2)
test('2h', 4)
test('2i', 8)
test('2l', 8)
test('2q', 16)
test('2B', 2)
test('2H', 4)

