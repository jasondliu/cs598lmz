import socket
socket.if_indextoname(3)

# get all interfaces
socket.if_nameindex()

# get all addresses
socket.getaddrinfo('www.python.org', 'http')

# get all addresses, with the canonical host name
socket.getaddrinfo('www.python.org', 'http', 0, 0, socket.SOL_TCP)

# getaddrinfo supports IPv6
socket.getaddrinfo('::1', 0, socket.AF_INET6, 0, 0, 0)

# getnameinfo supports IPv6
socket.getnameinfo(('::1', 80, 0, 0), 0)

# create a TCP socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to the server
s.connect(('www.python.org', 80))

# send some data
s.sendall(b'GET / HTTP/1.1\r\nHost: www.python.org\r\n\r\n')

# receive the response (in small chunks)
while True:
    chunk = s.recv
