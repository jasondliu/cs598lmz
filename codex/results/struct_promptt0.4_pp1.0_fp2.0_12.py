import _struct
# Test _struct.Struct()

def test(fmt, *args):
    s = _struct.Struct(fmt)
    print(s.size)
    print(s.pack(*args))
    print(s.unpack(s.pack(*args)))

test('h', 1)
test('l', 2)
test('q', 3)
test('h', 1, 2)
test('hh', 1, 2)
test('hh', 1, 2, 3)
test('hhh', 1, 2, 3)
test('hhhh', 1, 2, 3, 4)
test('hhhh', 1, 2, 3, 4, 5)
test('hhhhh', 1, 2, 3, 4, 5)
test('hhhhhh', 1, 2, 3, 4, 5, 6)
test('hhhhhhh', 1, 2, 3, 4, 5, 6, 7)
test('hhhhhhhh', 1, 2, 3, 4, 5, 6, 7, 8)
test('hhhhhhhh', 1, 2, 3, 4, 5, 6, 7, 8, 9)
test('hhhhhhhhh', 1,
