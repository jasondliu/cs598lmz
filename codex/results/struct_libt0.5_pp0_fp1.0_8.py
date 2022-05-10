import _struct
from _struct import *

def get_value(format, data, offset=0):
    size = calcsize(format)
    return unpack_from(format, data, offset)[0]

def get_byte(data, offset=0):
    return get_value("B", data, offset)

def get_word(data, offset=0):
    return get_value("H", data, offset)

def get_dword(data, offset=0):
    return get_value("I", data, offset)

def get_qword(data, offset=0):
    return get_value("Q", data, offset)

def get_string(data, offset=0, size=0):
    if size == 0:
        size = len(data)
    return get_value("{}s".format(size), data, offset)

def get_cstring(data, offset=0):
    size = 0
    while data[offset + size] != 0x00:
        size += 1
    return get_string(data, offset, size)
