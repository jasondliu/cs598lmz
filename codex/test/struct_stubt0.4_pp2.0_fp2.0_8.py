from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'i'
s.size = 4
s.pack(1)

# struct.Struct.__new__(format)
s = Struct('i')
s.pack(1)

# struct.Struct.__new__(format, name)
s = Struct('i', 'test')
s.pack(1)

# struct.Struct.__new__(format, name, *, byteorder)
s = Struct('i', 'test', byteorder='>')
s.pack(1)

# struct.Struct.__new__(format, *, byteorder)
s = Struct('i', byteorder='>')
s.pack(1)

# struct.Struct.__new__(format, name, *, byteorder, *, set=True)
s = Struct('i', 'test', byteorder='>', set=True)
s.pack(1)

# struct.Struct.__new__(format, name, *, byteorder, *, set=False)
