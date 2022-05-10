import socket
socket.if_indextoname(3)

socket.if_nameindex()

socket.if_nametoindex('lo')

socket.getaddrinfo('www.python.org', 'http')

socket.getaddrinfo('www.python.org', 'http', socket.AF_INET,
                   socket.SOCK_STREAM, 0, socket.AI_PASSIVE)

socket.getaddrinfo('www.python.org', 'http', socket.AF_INET,
                   socket.SOCK_STREAM, 0, socket.AI_PASSIVE,
                   socket.AI_ADDRCONFIG)

socket.getaddrinfo('www.python.org', 'http', socket.AF_INET,
                   socket.SOCK_STREAM, 0, socket.AI_PASSIVE,
                   socket.AI_ADDRCONFIG | socket.AI_V4MAPPED)

socket.getaddrinfo('www.python.org', 'http', socket.AF_INET,
                   socket.SOCK_STREAM, 0, socket.AI_PASSIVE,
                   socket.AI_ADDRCONFIG |
