import _struct

def pack(format, *args):
    return _struct.pack(format, *args)

def unpack(format, string):
    return _struct.unpack(format, string)

def calcsize(format):
    return _struct.calcsize(format)
