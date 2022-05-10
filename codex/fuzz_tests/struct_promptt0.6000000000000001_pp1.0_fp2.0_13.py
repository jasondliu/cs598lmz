import _struct
# Test _struct.Struct

import sys

def test(fmt, *args):
    print fmt, '->',
    print tuple(map(repr, _struct.calcsize_tuple(fmt))),
    print tuple(map(repr, _struct.pack_tuple(fmt, *args))),
    print tuple(map(repr, _struct.unpack_tuple(fmt, _struct.pack_tuple(fmt, *args))))

# Formats
test('b')
test('B')
test('h')
test('H')
test('i')
test('I')
test('l')
test('L')
test('q')
test('Q')
test('f')
test('d')
test('s')
test('p')
test('P')

# Repeat count
test('2b', 1, 2)
test('0b')
test('2b', 1)

# Native vs standard
if sys.byteorder == 'little':
    test('<b', 1)
    test('@b', 1)
    test('>
