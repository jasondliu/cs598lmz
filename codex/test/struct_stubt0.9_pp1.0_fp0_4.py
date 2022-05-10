from _struct import Struct
s = Struct.__new__(Struct)
s.__init__("Bh")
s.pack(0x00, 0x00, 0x0FAC)
