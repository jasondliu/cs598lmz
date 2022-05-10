from _struct import Struct
s = Struct.__new__(Struct)
s.format = '>I'
s.size = Struct.calcsize(s.format)

def read_int(f):
    print(f.read(s.size))
    return s.unpack(f.read(s.size))[0]

def read_data(f, size):
    return f.read(size)

def read_string(f):
    size = read_int(f)
    return read_data(f, size)

