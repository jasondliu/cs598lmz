import _struct
# Test _struct.Struct interface
import StringIO
import unittest
import struct
import sys

endianess = sys.byteorder

formats = {
    'x'     : 0.5,
    'c'     : b'x',
    'b'     : -100,
    'B'     : 200,
    '?'     : True,
    'h'     : -10000,
    'H'     : 10000,
    'i'     : -1000000000,
    'I'     : 1000000000,
    'l'     : -1000000000,
    'L'     : 1000000000,
    'q'     : -1000000000000000000,
    'Q'     : 10000000000000000000,
    'f'     : 3.125,
    'd'     : 987654321.5,
    's'     : "@ABC",
    'p'     : "@ABC",
    'P'     : 5
    }

def formats_little_endian():
    formats_copy = formats.copy()
