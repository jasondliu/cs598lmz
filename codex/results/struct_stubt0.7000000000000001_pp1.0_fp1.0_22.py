from _struct import Struct
s = Struct.__new__(Struct)
s.format = "i"
s.size = 4

def unpack(fmt, data):
    s.format = fmt
    return s.unpack_from(data)

def pack(fmt, *args):
    s.format = fmt
    return s.pack(*args)

import struct

def unpack(fmt, data):
    size = struct.calcsize(fmt)
    return struct.unpack(fmt, data[:size]), data[size:]

def pack(fmt, *args):
    return struct.pack(fmt, *args)


"""

"""

import struct

def unpack(fmt, data):
    size = struct.calcsize(fmt)
    return struct.unpack(fmt, data[:size]), data[size:]

def pack(fmt, *args):
    return struct.pack(fmt, *args)



"""

"""

import struct

def unpack(fmt, data):
    return struct.unpack(fmt, data
