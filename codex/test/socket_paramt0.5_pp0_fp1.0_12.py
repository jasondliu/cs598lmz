import socket
socket.if_indextoname(3)

print(socket.if_indextoname(3))

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind(('', 50000))

while True:
    data, address = s.recvfrom(65535)
    print(data)
    print(address)

#s.bind(('', 50000))

#s.listen(1)

#while True:
#    conn, addr = s.accept()
#    print(conn, addr)
#    print(conn.recv(1024))
#    conn.sendall(b'welcome')
