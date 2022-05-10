import _struct
# Test _struct.Struct.

import struct

from test import support

# Some basic tests to check that the module is working.

# These should all succeed.

struct.pack('h', 1)
struct.pack('i', 1)
struct.pack('l', 1)
struct.pack('q', 1)
struct.pack('H', 1)
struct.pack('I', 1)
struct.pack('L', 1)
struct.pack('Q', 1)
struct.pack('f', 1)
struct.pack('d', 1)
struct.pack('P', 1)

struct.unpack('h', b'\x00\x01')
struct.unpack('i', b'\x00\x00\x00\x01')
struct.unpack('l', b'\x00\x00\x00\x01')
struct.unpack('q', b'\x00\x00\x00\x00\x00\x00\x00\x01')
struct.unpack('H', b'\x00\x01')
struct.unpack('I
