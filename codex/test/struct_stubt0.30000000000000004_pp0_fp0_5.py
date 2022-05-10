from _struct import Struct
s = Struct.__new__(Struct)
s.size = lambda: 8
s.format = lambda: 'd'

def unpack(data):
    return s.unpack(data)[0]

def pack(value):
    return s.pack(value)

def pack_into(buffer, offset, value):
    return s.pack_into(buffer, offset, value)

def unpack_from(buffer, offset):
    return s.unpack_from(buffer, offset)[0]

def calcsize():
    return s.size

def new_double(value):
    return pack(value)

def new_double_array(size):
    return bytearray(size * 8)

def set_double(array, index, value):
    pack_into(array, index * 8, value)

def get_double(array, index):
    return unpack_from(array, index * 8)

def new_double_array_from_list(list):
    array = new_double_array(len(list))
