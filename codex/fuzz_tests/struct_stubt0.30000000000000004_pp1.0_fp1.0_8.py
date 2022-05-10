from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>i')
s.size

s.pack(1)

s.unpack(b'\x00\x00\x00\x01')

s.unpack(b'\x00\x00\x00\x01')[0]

s.unpack_from(b'\x00\x00\x00\x01\x00\x00\x00\x02', 4)

s.unpack_from(b'\x00\x00\x00\x01\x00\x00\x00\x02', 4)[0]

import socket
import struct

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('www.sina.com.cn', 80))
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

buffer = []
while True:
    d = s.recv
