import socket
socket.if_indextoname(19)

# inet_ntoa
import socket
socket.inet_ntoa(3958228234)
socket.inet_ntoa(b'\x01\x02\x03\x04')
socket.inet_ntoa(b'\x00\x00\x00\x00')  # only the first 1 byte is used

# inet_aton
import socket
socket.inet_aton(b'1.1.1.1')
socket.inet_aton(b'256.256.256.256')
socket.inet_aton(b'a.a.a.a')

# getservbyname
import socket
socket.getservbyname('telnet', 'tcp')
socket.getservbyname('telnet', 'udp')
socket.getservbyname('http')
socket.getservbyname('http', 'tcp')
socket.getservbyname('https')

# getprotobyname
import socket
socket.getprotobyname('icmp')
socket.getprotobyname('ip')
socket.getprot
