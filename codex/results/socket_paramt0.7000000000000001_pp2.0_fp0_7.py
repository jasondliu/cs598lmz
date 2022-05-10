import socket
socket.if_indextoname(10)
 
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('0.0.0.0', 54321))
s.setsockopt(socket.SOL_SOCKET, socket.SO_BINDTODEVICE, 'eth0')
 
while True:
    print s.recvfrom(1024)
