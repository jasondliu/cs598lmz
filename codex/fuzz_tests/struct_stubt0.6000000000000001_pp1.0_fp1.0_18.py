from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>I', 'data')
s.size

# from _struct import *
# unpack('>I', '\x00\x00\x00\x00')

from _struct import unpack
unpack('>I', '\x00\x00\x00\x00')

def unpack_from(fmt, buf, offset=0):
    return unpack(fmt, buffer(buf, offset))
pack_into = Struct.__new__(Struct).__init__('>I', 'data').pack_into

import binascii
binascii.hexlify(pack_into(b'\x00\x00\x00\x00', 4))
binascii.hexlify(unpack_from('>I', b'\x00\x00\x00\x00', 4))

from _struct import *
unpack('>I', '\x00\x00\x00\x00')

from _struct import *
unpack('>I', b'\x00\
