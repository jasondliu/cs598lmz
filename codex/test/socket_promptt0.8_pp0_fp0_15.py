import socket
# Test socket.if_indextoname()
socket.if_indextoname(1)

# $ nc -l -p 1234
# $ python3 1.py
# b'\x03\x00\x00\x00hello'

import socket
import struct

msg = struct.pack('!I6s', 1, b'world!')
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto(msg, ('localhost', 1234))

# $ nc -l -p 1234
# $ python3 1.py
# ('world!', ('127.0.0.1', 54506))

import socket
import struct

msg, addr = s.recvfrom(1024)
print(struct.unpack('!I6s', msg), addr)

# $ nc -l -p 1234
# $ python3 1.py
# b'\x03\x00\x00\x00hello'

import socket
import struct

