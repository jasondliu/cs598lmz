from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')

def pack(x):
    return s.pack(x)

def unpack(x):
    return s.unpack(x)[0]

def size():
    return s.size

def format():
    return s.format

def pack_into(buf, offset, x):
    return s.pack_into(buf, offset, x)

def unpack_from(buf, offset):
    return s.unpack_from(buf, offset)[0]
