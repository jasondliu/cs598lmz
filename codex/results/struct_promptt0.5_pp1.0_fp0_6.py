import _struct
# Test _struct.Struct.

def test(fmt, *args):
    s = _struct.Struct(fmt)
    print 'size:', s.size
    print 'pack:', s.pack(*args)
    print 'unpack:', s.unpack(s.pack(*args))
    print

test('i', 1)
test('i', -1)
test('i', 0x7fffffff)
test('i', -0x80000000)

test('l', 1)
test('l', -1)
test('l', 0x7fffffff)
test('l', -0x80000000)
test('l', 0x7fffffffffffffff)
test('l', -0x8000000000000000)

test('h', 1)
test('h', -1)
test('h', 0x7fff)
test('h', -0x8000)

test('b', 1)
test('b', -1)
test('b', 127)
test('b', -128)

test('c', 'x')
test('c', '\x00')
