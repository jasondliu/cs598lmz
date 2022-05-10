import _struct
# Test _struct.Struct with all of its explicit format characters.
# XXX More tests would be good.

def test(fmt, expected):
    s = _struct.Struct(fmt)
    got = s.size
    if got != expected:
        raise ValueError("%r: expected %d, got %d" % (fmt, expected, got))

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
test('P', 4)

# Non-native size/alignment

if _struct.calcsize("=i") != 4:
    raise ValueError("native i != 4")
if _struct.calcsize("=q") != 8:
    raise ValueError
