import socket
socket.if_indextoname(s.getsockopt(socket.SOL_SOCKET, socket.SO_BINDTODEVICE))

s.bind(saddr)
s.sendto(b'\x64\x32\x01\x12', daddr)



s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BINDTODEVICE, b'eth1'+'\0')
daddr = ('10.100.4.3', 22)
saddr = ('10.100.4.1', 0)
socket.if_indextoname(s.getsockopt(socket.SOL_SOCKET, socket.SO_BINDTODEVICE))

s.bind(saddr)

s.sendto('\x64\x32\x01\x12', daddr)
s.sendto('\x64\x32\x01\x12', daddr)
