import _struct
# Test _struct.Struct.format_size()

def test(fmt, expected):
    s = _struct.Struct(fmt)
    actual = s.format_size()
    if actual != expected:
        print('error in format %r: expected %d, got %d' % (fmt, expected, actual))

test('', 0)
test('x', 1)
test('b', 1)
test('c', 1)
test('bx', 2)
test('bxx', 3)
test('bxxx', 4)
test('bxxxx', 5)
test('bxxxxx', 6)
test('bxxxxxx', 7)
test('bxxxxxxx', 8)
test('bxxxxxxxx', 9)
test('bxxxxxxxxx', 10)
test('bxxxxxxxxxx', 11)
test('bxxxxxxxxxxx', 12)
test('bxxxxxxxxxxxx', 13)
test('bxxxxxxxxxxxxx', 14)
test('bxxxxxxxxxxxxxx', 15)
test('bxxxxxxxxxxxxxxx', 16)
test('bxxxxxxxxxxxxxxxx', 17)
test('bxxxxxxxxxxxxxxxxx', 18)
test('bxxxxxxxx
