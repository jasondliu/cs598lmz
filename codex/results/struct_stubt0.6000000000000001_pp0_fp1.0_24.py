from _struct import Struct
s = Struct.__new__(Struct)
s.format = "!I"
s.size = 4
def read_int(data, i):
    return s.unpack_from(data, i)[0]

def read_string(data, i):
    length = read_int(data, i)
    i += 4
    return (data[i:i+length], i+length)

def read_array(data, i):
    n = read_int(data, i)
    i += 4
    res = []
    for j in range(n):
        value, i = read_value(data, i)
        res.append(value)
    return (res, i)

def read_table(data, i):
    n = read_int(data, i)
    i += 4
    res = {}
    for j in range(n):
        key, i = read_value(data, i)
        value, i = read_value(data, i)
        res[key] = value
    return (res, i)

def read_value(data, i):

