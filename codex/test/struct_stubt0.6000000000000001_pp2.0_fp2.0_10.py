from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i', [])
s.unpack(b'\x00\x00\x00\x00')
