from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('<h')
s.unpack(b'\x01\x00')[0]

from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('<i')
s.unpack(b'\x01\x00\x00\x00')[0]

from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('<q')
s.unpack(b'\x01\x00\x00\x00\x00\x00\x00\x00')[0]

from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('<f')
s.unpack(b'\x01\x00\x00\x00')[0]

from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('<d')
