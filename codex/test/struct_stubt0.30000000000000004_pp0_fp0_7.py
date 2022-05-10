from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('I 2s f')
s.size

s.pack(1, 'ab'.encode('utf-8'), 2.7)

s.unpack(_)

s.unpack_from(bytes(range(12)), 4)

s = Struct('iif')
s.pack(1, 2, 3.0)

import struct
struct.pack('>iif', 1, 2, 3.0)

struct.unpack('>iif', _)

struct.unpack('>iif', bytes(range(12)))

struct.unpack_from('>iif', bytes(range(12)), 4)

struct.calcsize('>iif')

import binascii
binascii.hexlify(b'\x00\x01\x02\x03')

binascii.unhexlify(_)

import base64
base64.b64encode(b'binary\x00string')

base64.b64decode(_)

