import _struct
# Test _struct.Struct.__init__()

import struct
import sys

def test(fmt, bigendian=False, native=False):
    if bigendian:
        fmt = '>' + fmt
    elif native:
        fmt = '=' + fmt
    else:
        fmt = '<' + fmt
    s = _struct.Struct(fmt)
    print(s.format, s.size, s.pack('\0'*s.size))

test('x')
test('c')
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
test('cx')
test('cb')
test('cB')
test('cH')
test('ci')
test('cI')
test('cl')
test('cL')
test('cq')
test('cQ')
test('cf
