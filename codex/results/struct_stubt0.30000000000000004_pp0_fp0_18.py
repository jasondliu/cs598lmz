from _struct import Struct
s = Struct.__new__(Struct)
s.__dict__.update(Struct.__dict__)
s.format = '<3s3sHH'
s.size = s.calcsize(s.format)

def unpack_from(buffer, offset=0):
    return s.unpack_from(buffer, offset)

def pack_into(buffer, offset, host, port):
    return s.pack_into(buffer, offset, host, port)

def pack(host, port):
    return s.pack(host, port)

def unpack(buffer):
    return s.unpack(buffer)

def calcsize():
    return s.calcsize()

def test():
    import socket
    import binascii
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('8.8.8.8', 53))
    ip = s.getsockname()[0]
    s.close()
    host, port = ip, 53
    buf = pack(host, port)
    print
