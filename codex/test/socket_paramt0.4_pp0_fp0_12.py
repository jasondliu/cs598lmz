import socket
socket.if_indextoname(1)

socket.if_nametoindex('lo0')

socket.gethostname()

socket.gethostbyname('localhost')

socket.gethostbyname_ex('localhost')

socket.gethostbyaddr('127.0.0.1')

socket.getaddrinfo('localhost', 80)

socket.getaddrinfo('localhost', 80, socket.AF_INET, socket.SOCK_STREAM)

socket.getaddrinfo('localhost', 80, socket.AF_INET, socket.SOCK_STREAM, 0, socket.AI_PASSIVE)

socket.getaddrinfo('localhost', 80, socket.AF_INET, socket.SOCK_STREAM, 0, socket.AI_PASSIVE, socket.IPPROTO_IP)

socket.getaddrinfo('localhost', 80, socket.AF_INET, socket.SOCK_STREAM, 0, socket.AI_PASSIVE, socket.IPPROTO_IP, socket.IPPORT_RESERVED)

