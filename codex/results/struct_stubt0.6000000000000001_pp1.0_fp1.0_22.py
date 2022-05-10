from _struct import Struct
s = Struct.__new__(Struct)
s.__init__(">i")

def read_int(stream):
    return s.unpack(stream.read(4))[0]

def write_int(stream, n):
    stream.write(s.pack(n))

def read_string(stream):
    size = read_int(stream)
    return stream.read(size).decode()

def write_string(stream, s):
    write_int(stream, len(s))
    stream.write(s.encode())

def read_tuple(stream):
    size = read_int(stream)
    return tuple(read_string(stream) for i in range(size))

def write_tuple(stream, t):
    write_int(stream, len(t))
    for i in t:
        write_string(stream, i)

def write_list(stream, l):
    write_int(stream, len(l))
    for i in l:
        write_string(stream, i)

def read_list(stream):
    size
