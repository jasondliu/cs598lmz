from _struct import Struct
s = Struct.__new__(Struct)
s.format = '<3s3sHH'
s.size = calcsize(s.format)

def unpack_from(buffer, offset=0):
    return s.unpack_from(buffer, offset)

def pack_into(buffer, offset, host, port, hlen, plen):
    return s.pack_into(buffer, offset, host, port, hlen, plen)

def pack(host, port, hlen, plen):
    return s.pack(host, port, hlen, plen)

def unpack(buffer):
    return s.unpack(buffer)

def calcsize():
    return s.size

def get_size():
    return s.size

def get_format():
    return s.format

def get_struct():
    return s

def get_unpack_from():
    return unpack_from

def get_pack_into():
    return pack_into

def get_pack():
    return pack

def get_unpack():
    return unpack
