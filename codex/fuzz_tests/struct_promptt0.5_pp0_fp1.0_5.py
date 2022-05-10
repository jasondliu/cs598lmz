import _struct
# Test _struct.Struct.

def test(fmt, expected):
    s = _struct.Struct(fmt)
    got = s.size
    if got != expected:
        raise ValueError('%r: expected %d, got %d' % (fmt, expected, got))

test('xxxx', 16)
test('xxxxx', 20)
test('xxxxxx', 24)
test('xxxxxxx', 24)
test('xxxxxxxx', 32)
test('xxxxxxxxx', 40)
test('xxxxxxxxxx', 40)
test('xxxxxxxxxxx', 40)
test('xxxxxxxxxxxx', 48)
test('xxxxxxxxxxxxx', 48)
test('xxxxxxxxxxxxxx', 48)
test('xxxxxxxxxxxxxxx', 48)
test('xxxxxxxxxxxxxxxx', 64)
test('xxxxxxxxxxxxxxxxx', 64)
test('xxxxxxxxxxxxxxxxxx', 64)
test('xxxxxxxxxxxxxxxxxxx', 64)
test('xxxxxxxxxxxxxxxxxxxx', 64)
test('xxxxxxxxxxxxxxxxxxxxx', 64)
test('xxxxxxxxxxxxxxxxxxxxxx', 64)
test('xxxxxxxxxxxxxxxxxxxxxxx', 64)
test('xxxxxxxxxxxxxxxxxxxxxxxx', 64)
test('xxxxxxxxxxxxxxxxxxxxxxxxx', 64)
test
