import socket
socket.if_indextoname(i)
'eth0'

>>> socket.inet_aton('127.0.0.1')
b'\x7f\x00\x00\x01'
>>> socket.inet_ntoa(b'\x7f\x00\x00\x01')
'127.0.0.1'

>>> addrinfo = socket.getaddrinfo('127.0.0.1', 80, 0, 0, socket.SOL_TCP)
>>> addrinfo
[(2, 1, 6, '', ('127.0.0.1', 80))]
>>> af, socktype, proto, canonname, sa = addrinfo[0]
>>> af
2
>>> sa
('127.0.0.1', 80)

>>> sock = socket.socket(af, socktype, proto)
>>> sock.connect(sa)
'''

# 服务器端
import socket
host = '' # 代表0.0.0.0: 所有地址
port = 12345 # 1-65535
