from _struct import Struct
s = Struct.__new__(Struct)
s.format = '>i'
s.size = Struct.calcsize(s.format)

def read_int(data):
    return s.unpack(data.read(s.size))[0]

def read_string(data):
    length = read_int(data)
    return data.read(length)

def read_bytes(data):
    length = read_int(data)
    return data.read(length)

def read_array(data):
    length = read_int(data)
    return [read_value(data) for _ in range(length)]

def read_value(data):
    type = read_int(data)
    if type == 0:
        return None
    elif type == 1:
        return read_int(data)
    elif type == 2:
        return read_string(data)
    elif type == 3:
        return read_bytes(data)
    elif type == 4:
        return read_array(data)
