from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>I')
s.size
s.pack(1)
s.unpack(b'\x00\x00\x00\x01')
s.unpack(b'\x00\x00\x00\x01')[0]
s.unpack(b'\x00\x00\x00\x01')[0] == 1
s.unpack(b'\x00\x00\x00\x01')[0] == 2

# Exercise 2
from socket import socket, AF_INET, SOCK_STREAM

def recv_all(sock, length):
    data = b''
    while len(data) < length:
        more = sock.recv(length - len(data))
        if not more:
            raise EOFError('was expecting %d bytes but only received'
                           ' %d bytes before the socket closed'
                           % (length, len(data)))
        data += more
    return data

def server(interface, port):
    sock = socket(AF_IN
