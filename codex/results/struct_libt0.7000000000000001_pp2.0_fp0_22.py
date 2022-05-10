import _struct
import struct

def pack(fmt, *args):
    return _struct.pack(fmt, *args)

def unpack(fmt, string):
    return _struct.unpack(fmt, string)

def calcsize(fmt):
    return _struct.calcsize(fmt)
