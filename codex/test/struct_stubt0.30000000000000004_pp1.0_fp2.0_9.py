from _struct import Struct
s = Struct.__new__(Struct)
s.format = '>2i'
s.size = s.calcsize(s.format)
s.unpack = s.unpack_from
s.pack = s.pack

def read_int(f):
    return s.unpack(f.read(s.size))[0]

def read_ints(f, n):
    return s.unpack(f.read(s.size*n))

def read_float(f):
    return s.unpack(f.read(s.size))[1]

def read_floats(f, n):
    return s.unpack(f.read(s.size*n))[1:]

def read_string(f):
    n = read_int(f)
    return f.read(n).decode('utf-8')

def read_strings(f, n):
    return [read_string(f) for i in range(n)]

def write_int(f, x):
    f.write(s.pack(x, 0))

