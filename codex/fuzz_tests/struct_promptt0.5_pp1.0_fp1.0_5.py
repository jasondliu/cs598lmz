import _struct
# Test _struct.Struct

import struct
import sys

def test(fmt):
    print 'format:', fmt, 'returned:', _struct.calcsize(fmt), 'expected:', struct.calcsize(fmt)

test('i')
test('ii')
test('i'*10)
test('f')
test('d')
test('f'*10)
test('d'*10)
test('ifd')
test('ifd'*10)
test('c')
test('cc')
test('c'*10)
test('ccc')
test('ccc'*10)
test('cccc')
test('cccc'*10)
test('ccccc')
test('ccccc'*10)
test('cccccc')
test('cccccc'*10)
test('ccccccc')
test('ccccccc'*10)
test('cccccccc')
test('cccccccc'*10)
test('ccccccccc')
test('ccccccccc'*10)
test('
