from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('&gt;H')
s.unpack(b'\x00\x0f')
(15,)
