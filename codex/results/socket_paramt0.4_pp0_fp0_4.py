import socket
socket.if_indextoname(3)

socket.if_nametoindex("en0")

socket.getaddrinfo("www.python.org", "http", proto=socket.IPPROTO_TCP)

socket.getaddrinfo("127.0.0.1", 8080, proto=socket.IPPROTO_TCP)

socket.getaddrinfo("localhost", 8080, proto=socket.IPPROTO_TCP)

socket.getaddrinfo("localhost", 8080, proto=socket.IPPROTO_TCP, flags=socket.AI_NUMERICSERV)

socket.getaddrinfo("localhost", "http", proto=socket.IPPROTO_TCP, flags=socket.AI_NUMERICSERV)

socket.getaddrinfo("localhost", "http", proto=socket.IPPROTO_TCP, flags=socket.AI_NUMERICSERV | socket.AI_NUMERICHOST)

socket.getaddrinfo("localhost", "http", proto=socket.IPPROTO_TCP, flags=socket.AI_NUMERICSERV | socket.AI_NUM
