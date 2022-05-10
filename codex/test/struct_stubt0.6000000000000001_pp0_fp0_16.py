from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('I2s')
s.size

s = Struct('I 2s')
s.size

import binascii
s = Struct('I 2s f')
values = (1, 'ab'.encode('utf-8'), 2.7)
print(s.pack(*values))

print(binascii.hexlify(s.pack(*values)))

print(s.unpack(b'\x01\x00\x00\x00ab\x00\x00\x00\x00\x00\x00@?\x99\x99\x99\x99\x99\x9a'))

print(s.unpack_from(b'\x00\x00\x00\x00\x01\x00\x00\x00ab\x00\x00\x00\x00\x00\x00@?\x99\x99\x99\x99\x99\x9a', 4))
