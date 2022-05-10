from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'i'
s.size = 4
s.unpack = Struct.unpack
s.pack = Struct.pack

def read_int(stream):
    return s.unpack(stream.read(s.size))[0]

def write_int(stream, value):
    stream.write(s.pack(value))

def read_string(stream):
    length = read_int(stream)
    return stream.read(length).decode('utf-8')

def write_string(stream, value):
    write_int(stream, len(value))
    stream.write(value.encode('utf-8'))

def read_data(stream):
    length = read_int(stream)
    return stream.read(length)

def write_data(stream, value):
    write_int(stream, len(value))
    stream.write(value)

def read_list(stream, read_element):
    length = read_int(stream)
