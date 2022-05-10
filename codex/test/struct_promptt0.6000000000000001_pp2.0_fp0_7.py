import _struct
# Test _struct.Struct()
def pack_test(fmt, *args):
    print(fmt, args)
    s = _struct.Struct(fmt)
    print(s.size)
    b = s.pack(*args)
    print(b)
    print(s.unpack(b))
    print(s.unpack_from(b, 0))
    print(s.unpack_from(b, 0, 1))
    
pack_test('i', 1)
pack_test('ii', 1, 2)
pack_test('iii', 1, 2, 3)

print('\n')

# Test _struct.calcsize()
def calcsize_test(fmt):
    print(fmt)
    print(_struct.calcsize(fmt))

calcsize_test('i')
calcsize_test('ii')
calcsize_test('iii')

print('\n')

# Test _struct.pack_into()
