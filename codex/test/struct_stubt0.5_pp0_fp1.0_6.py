from _struct import Struct
s = Struct.__new__(Struct)
s.format = '<I'
s.size = 4

def read_int(f):
    return s.unpack(f.read(4))[0]

def read_string(f):
    length = read_int(f)
    return f.read(length).decode('utf-8')

def read_list(f, fn):
    length = read_int(f)
    return [fn(f) for i in range(length)]

def read_dict(f, fn1, fn2):
    length = read_int(f)
    return {fn1(f): fn2(f) for i in range(length)}

def read_file(f):
    return {
        'name': read_string(f),
        'data': f.read(),
    }

def read_type(f):
    return {
        'name': read_string(f),
        'members': read_list(f, read_member),
    }

