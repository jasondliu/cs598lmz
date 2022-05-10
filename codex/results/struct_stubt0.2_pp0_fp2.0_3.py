from _struct import Struct
s = Struct.__new__(Struct)
s.format = '<3s3sHH'
s.size = s.calcsize(s.format)

def unpack_from(buffer, offset=0):
    return s.unpack_from(buffer, offset)

def pack_into(buffer, offset, host, port):
    return s.pack_into(buffer, offset, b'\x00\x00\x00', b'\x00\x00\x00', host, port)

def pack(host, port):
    return s.pack(b'\x00\x00\x00', b'\x00\x00\x00', host, port)

def unpack(buffer):
    return s.unpack(buffer)

def size():
    return s.size

def pack_addr(host, port):
    return pack(host, port)

def unpack_addr(buffer):
    return unpack(buffer)

def pack_addr_into(buffer, offset, host, port):
    return pack_into(buffer, offset, host, port)
