from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('Biii')
s.size

# both of these work:
b = s.pack(1, 2, 3, 4)
b = s.pack(b'\1', 2, 3, 4)

# but this doesn't:
b = s.pack(bytes([1]), 2, 3, 4)

# and this doesn't:
