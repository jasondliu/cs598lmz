from _struct import Struct
s = Struct.__new__(Struct)
s.format = '<hHI'
s._unpack=Unpack_asciiz
print s.unpack_from(binascii.unhexlify('000200006412'))
print s.unpack_from(binascii.unhexlify('000100116412'))
