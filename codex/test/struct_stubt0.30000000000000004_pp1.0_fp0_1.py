from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('iif')
s.size

# Create a new struct format string that is identical to the old one
s2 = Struct.__new__(Struct)
s2.__init__(s.format)
s2.size

# Create a struct that uses the same format as s, but in native byte order
s3 = Struct.__new__(Struct)
s3.__init__(s.format, s.format.encode('ascii'))
s3.size

# Create a struct that uses the same format as s, but in standard size and alignment
s4 = Struct.__new__(Struct)
s4.__init__(s.format, s.format.encode('ascii'), True)
s4.size

# Create a struct that uses the same format as s, but in standard size and alignment
s5 = Struct.__new__(Struct)
s5.__init__(s.format, s.format.encode('ascii'), True)
s5.size

# Create a struct that uses the same format as
