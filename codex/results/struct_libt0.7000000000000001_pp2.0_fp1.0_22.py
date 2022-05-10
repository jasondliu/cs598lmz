import _struct
import array
import struct
import sys

def main():
    s = array.array('b', [0x31, 0x32, 0x33, 0x34])
    print repr(s.tostring())

    a = array.array('i', xrange(3))
    print 'Initial :', a
    a.extend(xrange(3))
    print 'Extended:', a
    print 'Sliced  :', a[2:5]

    print 'Concatenate:', a + array.array('i', xrange(2))

    print 'Multiply:', a * 3

    print 'Iterate:'
    print list(enumerate(a))

    print 'Reverse:'
    a.reverse()
    print a

    print 'Read binary file:'
    a = array.array('i', open('data/array.bin', 'rb'))
    print 'A1:', a
    as_bytes = a.tostring()
    print 'A2:', array.array('i', as_bytes)

if __
