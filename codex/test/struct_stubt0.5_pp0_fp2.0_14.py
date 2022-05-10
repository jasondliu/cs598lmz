from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'hhl'
s.size = s.calcsize(s.format)
print(s.size)

import array
import binascii
numbers = array.array('h', [-2, -1, 0, 1, 2])
octets = bytes(numbers)
print(octets)
print(binascii.hexlify(octets))

octets = b'\x00\x00\x00\x07spam\x00\x08'
print(octets.find(b'spam'))
print(octets.find(b'spam', 5))

print(octets.rfind(b'\x00'))
print(octets.rfind(b'\x00', 3, -1))

print(octets.count(b'\x00'))
print(octets.count(b'\x00', 2, -1))

print(octets.startswith(b'\x00\x00\x00\x07'))
