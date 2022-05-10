import socket
socket.if_indextoname(3)

print socket.INADDR_ANY

a = socket.getaddrinfo('www.python.org', 80)
for x in a:
    print x
