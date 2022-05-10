import socket
# Test socket.if_indextoname()
# $ python3 -m http.server --bind 127.0.0.1 8001
# $ python3 test/test_socket_if_indextoname.py

HOST, PORT = '::1', 8001
ifname, ifindex = socket.if_indextoname(socket.if_nametoindex('lo')) # if_indextoname()
print('\nconnect() via lo ifindex %d' % ifindex)

sock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
sock.bind((HOST, PORT, 0, ifindex)) # ifindex
sock.listen(1)
print('listening on %s:%d' % (HOST, PORT))
conn, addr = sock.accept()
print('accepted connection from %s:%d' % addr)
print(sock.getsockname())
sock.close()
