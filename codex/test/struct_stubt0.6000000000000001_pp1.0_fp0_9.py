from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'hhl'
s.size = 8
s.pack(1,2,3)

import struct
struct.pack('>H', 1)
struct.pack('>H', 0x1234)
struct.pack('>H', 0xffff)
struct.unpack('>H', b'\x00\x01')
struct.unpack('>H', b'\x12\x34')
struct.unpack('>H', b'\xff\xff')

import struct
struct.unpack('>i', b'\x00\x01\x00\x00')
struct.unpack('>i', b'\x00\x01\x00\x00')[0]
struct.unpack('>i', b'\xff\xff\xff\xff')[0]
struct.unpack('>i', b'\xff\xff\xff\xff')

