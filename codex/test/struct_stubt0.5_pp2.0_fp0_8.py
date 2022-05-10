from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.size

#2.2
#coding=utf-8
from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.pack(1)

#2.3
#coding=utf-8
from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.pack(1)
s.unpack(b'\x01\x00\x00\x00')

#2.4
#coding=utf-8
from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.pack(1)
s.unpack(b'\x01\x00\x00\x00')
s.unpack_from(b'\x00\x00\x00\x01\x00\x00\x00', 4)

#2.5
#coding=utf-8
from _struct import Struct
