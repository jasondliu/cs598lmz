from _struct import Struct
s = Struct.__new__(Struct)
s.code = 'Q'
s.size = 8

def unpack(fmt, data):
    return s.unpack(data)

def pack(fmt, data):
    return s.pack(*data)

def load(f, offset, length):
    f.seek(offset)
    return unpack(f.read(length))

def dump(f, offset, data):
    f.seek(offset)
    f.write(pack(data))

def check_format(magic):
    return magic == MAGIC

def check_size(f, offset, length):
    return length == SIZE

def read(f, offset, length, cache={}, **kwargs):
    if not check_size(f, offset, length):
        raise Exception('invalid size')

    f.seek(offset)
    magic = f.read(4)

    if not check_format(magic):
        raise Exception('invalid format')

    version = unpack('<I', f.read(4))[0]

    if version != 1:

