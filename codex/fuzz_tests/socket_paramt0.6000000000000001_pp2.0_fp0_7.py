import socket
socket.if_indextoname(1)

socket.getnameinfo(('127.0.0.1', 8080), 0)

socket.getaddrinfo("www.baidu.com", 80, 0, 0, socket.IPPROTO_TCP)

socket.getaddrinfo("www.baidu.com", None)

socket.getaddrinfo("www.baidu.com", None, 0, 0, socket.IPPROTO_TCP, socket.AI_CANONNAME)

socket.getaddrinfo("::1", 80, socket.AF_INET6, socket.SOCK_STREAM, 0, socket.AI_PASSIVE)

socket.getaddrinfo("::1", 80, socket.AF_INET6, socket.SOCK_STREAM, 0, socket.AI_CANONNAME)

socket.getaddrinfo("::1", 80, socket.AF_INET6, socket.SOCK_STREAM, 0, socket.AI_NUMERICHOST)

socket.getaddrinfo("::1", 80, socket.AF_INET6, socket
