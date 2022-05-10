import _struct
# Test _struct.Struct.

def test(fmt):
    s = _struct.Struct(fmt)
    print(s.format)
    print(s.size)
    print(s.pack(*range(s.size)))
    print(s.unpack(s.pack(*range(s.size))))

test('c')
test('b')
test('h')
test('i')
test('l')
test('q')
test('f')
test('d')
test('s')
test('p')
test('P')

# Test _struct.Struct with keyword arguments.

def test_kw(fmt):
    s = _struct.Struct(fmt)
    print(s.format)
    print(s.size)
    print(s.pack(**dict([(str(i),i) for i in range(s.size)])))
    print(s.unpack(s.pack(**dict([(str(i),i) for i in range(s.size)]))))

test_kw('cc')
test_kw('bb')
test_kw
