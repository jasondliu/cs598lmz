from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('I 2s f')
s.size

import struct
struct.calcsize('I 2s f')

import struct
struct.pack('I 2s f', *(1, b'ab', 2.7))

import struct
struct.unpack('I 2s f', b'\x00\x00\x00\x01ab\x00\x00\x00@\x00\x00\x00')

import struct
struct.unpack('I 2s f', b'\x00\x00\x00\x01ab\x00\x00\x00@\x00\x00\x00')

import struct
struct.unpack('I 2s f', b'\x00\x00\x00\x01ab\x00\x00\x00@\x00\x00\x00')

import struct
struct.unpack('I 2s f', b'\x00\x00\x00\x01ab\x00\x00\x00@\x00\x00\
