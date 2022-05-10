from _struct import Struct
s = Struct.__new__(Struct)
s.__init__("<i")
s.pack(1)

# struct.Struct.__new__(struct.Struct)
# struct.Struct.__init__(<struct.Struct object at 0x7f5f5b9c5d48>, "<i")
# struct.Struct.pack(<struct.Struct object at 0x7f5f5b9c5d48>, 1)
# '\x01\x00\x00\x00'
