import _struct
# Test _struct.Struct

import sys

def test(fmt):
    s = _struct.Struct(fmt)
    print 'format:', fmt, 'size:', s.size
    data = s.pack(1, 2, 3)
    print 'data:', binascii.hexlify(data)
    try:
        s.pack()
    except TypeError:
        pass
    else:
        print 'expected exception'

    try:
        s.pack(1, 2, 3, 4)
    except TypeError:
        pass
    else:
        print 'expected exception'

    print 'unpack:', s.unpack(data)
    try:
        s.unpack('xxx')
    except TypeError:
        pass
    else:
        print 'expected exception'

print 'native:'
test('hhh')
test('iii')
test('qqq')
test('ddd')

print 'standard size:'
test('!hhh')
test('@iii')
test('=qqq')
test('<ddd')

print 'non-standard
