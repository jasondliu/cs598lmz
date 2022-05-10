import _struct
# Test _struct.Struct

# Test simple packing and unpacking

import struct
import _struct

def testPack(format, expected, value):
    result = _struct.pack(format, value)
    if result != expected:
        raise RuntimeError, 'pack failed; expected %r, got %r' % (expected, result)
    result = _struct.unpack(format, expected)[0]
    if result != value:
        raise RuntimeError, 'unpack failed; expected %r, got %r' % (value, result)

def testPackSize(format, expected):
    result = _struct.calcsize(format)
    if result != expected:
        raise RuntimeError, 'calcsize failed; expected %r, got %r' % (expected, result)

testPack('c', 'x', 'x')
testPack('c', '\x80', '\x80')
testPackSize('c', 1)

testPack('b', '\x00', 0)
testPack('b', '\x01', 1)
testPack('b', '\x7f', 127
