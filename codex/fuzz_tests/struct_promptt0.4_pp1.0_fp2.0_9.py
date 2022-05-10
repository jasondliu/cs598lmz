import _struct
# Test _struct.Struct().unpack()

import sys

def test(fmt, data, expected):
    s = _struct.Struct(fmt)
    result = s.unpack(data)
    if result != expected:
        print('error in %s.unpack(%r): expected %r, got %r' %
              (fmt, data, expected, result))

def test_all():
    test('i', b'\x00\x00\x00\x00', (0,))
    test('i', b'\x00\x00\x00\x01', (1,))
    test('i', b'\xff\xff\xff\xff', (-1,))
    test('i', b'\x7f\xff\xff\xff', (2147483647,))
    test('i', b'\x80\x00\x00\x00', (-2147483648,))
    test('i', b'\xff\xff\xff\x7f', (2147483647,))
    test('i', b'\
