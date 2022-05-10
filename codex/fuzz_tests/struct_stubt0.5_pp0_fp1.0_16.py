from _struct import Struct
s = Struct.__new__(Struct)
s.__init__("<2i")
s.pack(1, 2)

# another way to create a Struct object
Struct("<2i")
