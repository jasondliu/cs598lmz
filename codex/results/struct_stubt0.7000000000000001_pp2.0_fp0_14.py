from _struct import Struct
s = Struct.__new__(Struct)
s.set_format('@B')

def read_byte(f):
    return s.unpack_from(f.read(1))[0]

def read_int(f):
    return s.unpack_from(f.read(1))[0]

def read_short(f):
    return s.unpack_from(f.read(2))[0]

def read_float(f):
    return s.unpack_from(f.read(4))[0]

def read_double(f):
    return s.unpack_from(f.read(8))[0]

def read_string(f):
    size = read_int(f)
    if size <= 0:
        return ''
    return f.read(size)

def read_bool(f):
    return bool(read_byte(f))

def read_data(f):
    size = read_int(f)
    if size <= 0:
        return ''
    return f.read(size)


def write_byte(
