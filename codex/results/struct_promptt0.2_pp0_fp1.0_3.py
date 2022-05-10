import _struct
# Test _struct.Struct.format

import struct

def test(fmt, expected):
    s = _struct.Struct(fmt)
    if s.format != expected:
        print 'Error in format: expected %s, got %s' % (expected, s.format)

test('hhl', 'hhl')
test('hhh', 'hhh')
test('hhh', 'hhh')
test('bBhHiIlLqQfdspP', 'bBhHiIlLqQfdspP')
test('0p', '0p')
test('1p', '1p')
test('2p', '2p')
test('3p', '3p')
test('4p', '4p')
test('5p', '5p')
test('6p', '6p')
test('7p', '7p')
test('8p', '8p')
test('9p', '9p')
test('10p', '10p')
test('11p', '11p')
test('12p', '12p')
test('13p', '13p')
