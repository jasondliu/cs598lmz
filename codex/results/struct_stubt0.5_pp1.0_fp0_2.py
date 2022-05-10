from _struct import Struct
s = Struct.__new__(Struct)
s.__init__("<i")

def read_int(f):
    return s.unpack(f.read(4))[0]

def read_string(f):
    return f.read(read_int(f))

def length_of_string(s):
    return 4 + len(s)

def write_int(f, num):
    f.write(s.pack(num))

def write_string(f, s):
    write_int(f, len(s))
    f.write(s)

def read_int_array(f):
    return map(read_int, f)

def read_string_array(f):
    return map(read_string, f)

def write_int_array(f, arr):
    map(write_int, f, arr)

def write_string_array(f, arr):
    map(write_string, f, arr)

def read_int_matrix(f):
    return map(read_int_array, f)

def read
