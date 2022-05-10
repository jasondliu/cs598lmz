from _struct import Struct
s = Struct.__new__(Struct)
s.format = '>I'
s.size = s.calcsize('>I')
def read_integer(self): return s.unpack(self.file.read(s.size))[0]


# Version number is two unsigned four byte integers (major and minor)
s = Struct.__new__(Struct)
s.format = '>2I'
s.size = s.calcsize('>2I')
def read_version(self): return s.unpack(self.file.read(s.size))

# A code is two unsigned four byte integers (major and minor)
s = Struct.__new__(Struct)
s.format = '>2I'
s.size = s.calcsize('>2I')


def read_code(self):
    major,minor = s.unpack(self.file.read(s.size))
    return '%d.%d' % (major,minor)



# An enumerated is an unsigned four-byte integer
s = Struct.__new__(Struct)
s.format
