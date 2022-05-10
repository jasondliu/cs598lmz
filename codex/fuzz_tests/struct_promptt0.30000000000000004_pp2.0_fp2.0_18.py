import _struct
# Test _struct.Struct.unpack_from

import array

def test(fmt, data, expected):
    s = _struct.Struct(fmt)
    a = array.array('b', data)
    res = s.unpack_from(a, 0)
    if res != expected:
        print 'unpack_from(%r, %r) returned %r, expected %r' % (
            fmt, data, res, expected)

test('b', '\x01', (1,))
test('b', '\x01\x02', (1,))
test('h', '\x01\x02', (258,))
test('h', '\x01\x02\x03\x04', (258,))
test('i', '\x01\x02\x03\x04', (67305985,))
test('i', '\x01\x02\x03\x04\x05\x06\x07\x08', (67305985,))
test('l', '\x01\x02\x03\x04
