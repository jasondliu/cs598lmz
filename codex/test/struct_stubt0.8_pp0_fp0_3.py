from _struct import Struct
s = Struct.__new__(Struct)
s.format = '<I'
s.size = 4

def read_u32(f):
    return s.unpack(f.read(4))[0]

def read_str(f):
    return f.read(read_u32(f))

def write_u32(f, n):
    f.write(s.pack(n))

def write_str(f, s):
    write_u32(f, len(s))
    f.write(s)

def extract(f, first_offset):
    f.seek(first_offset)
    n = read_u32(f)
    offsets = [0] + [read_u32(f) for i in range(n)]
    m = read_u32(f)
    strings = {}
    f.seek(first_offset)
    for i in range(m):
        f.seek(offsets[i])
        string = read_str(f)
        strings[string] = i
    return strings

