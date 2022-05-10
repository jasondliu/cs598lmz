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

octets

octets.decode('iso8859_7')

octets.decode('koi8_r')

octets.decode('utf_8')

octets.decode('utf_8', errors='replace')

octets.decode('utf_8', errors='ignore')

from unicodedata import name
name('A')

name('\u00c6')

name('\u00c6'.encode('utf_8'))

name('\u00c6'.encode('cp1252'))

name('\u00c6'.encode('ascii', 'replace'))

