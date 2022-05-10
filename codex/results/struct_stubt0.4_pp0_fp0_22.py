from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'i'
s.size = 4

def pack(x):
    return s.pack(x)

def unpack(x):
    return s.unpack(x)[0]

def unpack_from(x, offset=0):
    return s.unpack_from(x, offset)[0]

def pack_into(x, offset, val):
    s.pack_into(x, offset, val)

def get_size():
    return s.size

def get_format():
    return s.format

def get_struct():
    return s

def get_native_type():
    return int

def get_native_format():
    return 'i'

def get_native_size():
    return 4

def get_native_struct():
    return Struct.__new__(Struct)
