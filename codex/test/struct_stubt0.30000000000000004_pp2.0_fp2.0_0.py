from _struct import Struct
s = Struct.__new__(Struct)
s.format = '<I'
s.size = 4
s.pack = Struct.__dict__['pack']
s.unpack = Struct.__dict__['unpack']
s.unpack_from = Struct.__dict__['unpack_from']

def get_int(data, offset):
    return s.unpack_from(data, offset)[0]

def get_int_le(data, offset):
    return s.unpack_from(data, offset)[0]

def get_int_be(data, offset):
    return s.unpack_from(data, offset)[0]

def get_uint(data, offset):
    return s.unpack_from(data, offset)[0]

def get_uint_le(data, offset):
    return s.unpack_from(data, offset)[0]

def get_uint_be(data, offset):
    return s.unpack_from(data, offset)[0]

