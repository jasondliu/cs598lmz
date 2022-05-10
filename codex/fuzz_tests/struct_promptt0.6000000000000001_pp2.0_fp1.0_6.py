import _struct
# Test _struct.Struct()
def test(fmt, *args):
    s = _struct.Struct(fmt)
    print 'size of', fmt, ':', s.size
    print 'format string:', s.format
    print 'packed value :', s.pack(*args)
    print 'unpacked value:', s.unpack(s.pack(*args))
    print

test('i', 123)
test('>i', 123)
test('<i', 123)
test('b', 123)
test('>b', 123)
test('<b', 123)
test('h', 123)
test('>h', 123)
test('<h', 123)
test('I', 123)
test('>I', 123)
test('<I', 123)
test('B', 123)
test('>B', 123)
test('<B', 123)
test('H', 123)
test('>H', 123)
test('<H', 123)
test('f', 123)
test('>f', 123)
test('<f', 123)
test('d', 123)

