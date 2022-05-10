from _struct import Struct
s = Struct.__new__(Struct) # This is the same as s=Struct()
s.__init__("<H", 2) # same as s.__init__("<H")
s.size # 2
s.format # "<H"
s.pack(1) # b'\x01\x00'
s.pack_into(1, b'\x00\x00\x00') # b'\x00\x01\x00'

s = Struct('!i3sf')
s.unpack(b'\x12\x34\x56\x78\x9A\xBC\xDE\xF1\x23\x45\x00\x00') 
# (305419896, b'\x9A\xBC\xDE', 1.7300000190734863)

import struct
struct.pack("!H", 1) # b'\x01\x00'
struct.unpack("!H", b'\x01\x00') # (1,)
