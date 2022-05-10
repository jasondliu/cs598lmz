from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i?f')
s.size

s = Struct('i?f')
s.size

import struct
struct.calcsize('i?f')

octets = b'Montr\xe9al'
octets

city = octets.decode('cp1252')
city

city.encode('cp1252')

octets.decode('iso8859_7')

octets.decode('koi8_r')

octets.decode('utf_8')

octets.decode('utf_16')

octets.decode('utf_8', errors='replace')

octets.decode('utf_8', errors='ignore')

u16 = 'El Niño'.encode('utf_16')
u16

list(u16)

u16.decode('utf_16')

u16le = 'El Niño'.encode('utf_16le')
u16le

u16be = 'El Niño'.encode('utf_16be')
u16be

