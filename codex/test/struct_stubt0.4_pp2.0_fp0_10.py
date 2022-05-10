from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('<i')

def read_int(f):
    return s.unpack(f.read(4))[0]

def read_int_list(f):
    return [read_int(f) for i in range(read_int(f))]

def read_int_matrix(f):
    return [read_int_list(f) for i in range(read_int(f))]

def write_int(f, i):
    f.write(s.pack(i))

def write_int_list(f, l):
    write_int(f, len(l))
    for i in l:
        write_int(f, i)

def write_int_matrix(f, m):
    write_int(f, len(m))
    for l in m:
        write_int_list(f, l)

def read_str(f):
    return f.read(read_int(f))

