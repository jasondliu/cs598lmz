from _struct import Struct
s = Struct.__new__(Struct)
s.size = lambda: 4
s.pack_into = lambda buf, offset, v: None
s.unpack_from = lambda buf, offset: None

# Python 3.2
from _socket import socket, AF_INET, SOCK_STREAM, SOCK_DGRAM, SOCK_RAW
s = socket.__new__(socket)
s.connect = lambda addr: None
s.bind = lambda addr: None
s.send = lambda data: None
s.sendto = lambda data, addr: None
s.sendmsg = lambda data, ancdata, flags: None
s.sendall = lambda data: None
s.recv = lambda bufsize: None
s.recv_into = lambda buf, nbytes: None
s.recvfrom = lambda bufsize: None
s.recvfrom_into = lambda buf, nbytes: None
s.recvmsg = lambda bufsize, ancbufsize: None
s.recvmsg_into = lambda buf, ancbuf, flags: None
s.getsockopt = lambda level, optname: None
s
