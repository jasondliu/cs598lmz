import _struct
# Test _struct.Struct.format_size()

def test(name, fmt, expected):
    s = _struct.Struct(fmt)
    got = s.format_size()
    if got != expected:
        raise ValueError("%s: size mismatch, expected %d, got %d" % (name, expected, got))

test('c', 'c', 1)
test('b', 'b', 1)
test('B', 'B', 1)
test('h', 'h', 2)
test('H', 'H', 2)
test('i', 'i', 4)
test('I', 'I', 4)
test('l', 'l', 4)
test('L', 'L', 4)
test('q', 'q', 8)
test('Q', 'Q', 8)
test('f', 'f', 4)
test('d', 'd', 8)
test('s', 's', 1)
test('p', 'p', 1)
print('Test passed.')
