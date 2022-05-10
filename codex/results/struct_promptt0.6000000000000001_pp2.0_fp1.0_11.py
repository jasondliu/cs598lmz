import _struct
# Test _struct.Struct and _struct.unpack_from

import struct
import sys

def test(fmt, data):
    print fmt, '<%r>' % data
    print repr(struct.pack(fmt, data))
    s = _struct.Struct(fmt)
    print repr(s.pack(data))
    print repr(s.pack_into(data, 0, data))
    print repr(s.unpack(s.pack(data)))
    print repr(s.unpack_from(s.pack(data), 0))
    print

def test2(fmt, data):
    s = _struct.Struct(fmt)
    print fmt, '<%r>' % data
    print repr(s.unpack(s.pack(data)))
    print repr(s.unpack_from(s.pack(data), 0))
    print

def main():
    print '-' * 75
    test('c', 'x')
    test('b', 10)
    test('b', -10)
    test('B', 10)
    test('
