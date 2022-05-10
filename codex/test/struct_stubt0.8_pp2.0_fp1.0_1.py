from _struct import Struct
s = Struct.__new__(Struct)
s.__init__("&lt;I")
a = s.pack(0x12345678)
