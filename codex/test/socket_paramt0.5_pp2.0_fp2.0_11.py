import socket
socket.if_indextoname(3)

#import socket
socket.gethostbyaddr('192.168.0.1')

#import socket
socket.gethostname()

#import socket
socket.gethostbyname('localhost')

#import socket
socket.gethostbyname_ex('localhost')

#import socket
socket.getservbyname('http')

#import socket
socket.getservbyport(80)

#import socket
socket.getaddrinfo('localhost', 80)

#import socket
socket.getaddrinfo('localhost', 80, socket.AF_INET)

#import socket
socket.getaddrinfo('localhost', 80, socket.AF_INET, socket.SOCK_STREAM)

#import socket
socket.getaddrinfo('localhost', 80, socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)

#import socket
socket.getaddrinfo('localhost', 80, socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP, socket.AI_CANONNAME)
