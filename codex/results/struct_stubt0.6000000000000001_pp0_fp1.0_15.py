from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>i')
s.pack(1)

# 使用Struct来解决字节序问题
import sys
import struct

def unpack_int32(f):
    data = f.read(4)
    return struct.unpack('>i',data)[0]


def unpack_float(f):
    data = f.read(4)
    return struct.unpack('>f',data)[0]


def unpack_string(f):
    raw_len = unpack_int32(f)
    if raw_len:
        data = f.read(raw_len)
        return data.decode('utf-8')
    else:
        return None

def unpack_record(f):
    kind = unpack_int32(f)
    time = unpack_float(f)
    level = unpack_string(f)
    message = unpack_string(f)
    return kind, time, level, message


def unpack_
