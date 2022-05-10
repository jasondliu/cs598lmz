from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.pack(1)

# struct.Struct.__new__(struct.Struct)
# struct.Struct.__init__(s, 'i')
# s.pack(1)

# struct.Struct.__new__(struct.Struct, 'i')
# s.pack(1)

# s = struct.Struct('i')
# s.pack(1)

# s = struct.Struct.__new__(struct.Struct, 'i')
# s.pack(1)

# s = struct.Struct.__new__(struct.Struct)
# s.__init__('i')
# s.pack(1)

# s = struct.Struct.__new__(struct.Struct, 'i')
# s.pack(1)

# s = struct.Struct.__new__(struct.Struct)
# s.__init__('i')
# s.pack(1)

# s = struct.Struct.__new__(struct.Struct)
# s.__init__('i')
# s
