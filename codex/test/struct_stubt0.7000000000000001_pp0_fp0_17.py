from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('I 2s f')
s.size



from _struct import Struct
from binascii import hexlify
s = Struct('>I 2s f')
values = (1, 'ab'.encode('utf-8'), 2.7)
print(s.pack(*values))
print(hexlify(s.pack(*values)))
print(s.unpack(b'\x00\x00\x00\x01ab\x00\x00\x00\x00\x00\x00@\x9a\x99\x99\x99\x99\x99\xf1?'))
