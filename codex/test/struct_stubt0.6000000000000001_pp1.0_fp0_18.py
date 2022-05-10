from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('some', 'random', 'args')
s
s.format
s.size
s.pack(1, 2, 3)
s.pack_into(bytearray(s.size), 0, 1, 2, 3)
s.unpack(s.pack(1, 2, 3))
