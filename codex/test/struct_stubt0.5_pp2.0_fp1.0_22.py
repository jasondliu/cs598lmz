from _struct import Struct
s = Struct.__new__(Struct)
s.format = '<2s2s'
s.size = s.calcsize(s.format)
s.unpack = s.unpack_from
s.pack = s.pack

def get_short(data, offset):
    return s.unpack(data, offset)[0]

def get_byte(data, offset):
    return data[offset]

def get_int(data, offset):
    return i.unpack(data, offset)[0]

def get_long(data, offset):
    return l.unpack(data, offset)[0]

def get_float(data, offset):
    return f.unpack(data, offset)[0]

def get_double(data, offset):
    return d.unpack(data, offset)[0]

def get_string(data, offset):
    length = get_byte(data, offset)
    offset += 1
    return (data[offset:offset+length], offset + length)

