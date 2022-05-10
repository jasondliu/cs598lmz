import socket
socket.if_indextoname(2)

socket.gethostbyname('www.google.com')

# socket.gethostbyname_ex('www.google.com')

socket.gethostbyaddr('216.58.219.206')

socket.getnameinfo(('216.58.219.206', 80), 0)

socket.getaddrinfo('www.google.com', 80)

socket.getaddrinfo('www.google.com', 80, 0, 0, socket.IPPROTO_TCP)

socket.getaddrinfo('www.google.com', 80, 0, 0, socket.IPPROTO_TCP, socket.AI_CANONNAME)

socket.getaddrinfo('www.google.com', None)

socket.getaddrinfo('ipv6.google.com', 80, socket.AF_INET6, 0, socket.IPPROTO_TCP)

socket.getaddrinfo('ipv6.google.com', 80, socket.AF_INET6, 0, socket.IPPROTO_TCP, socket.AI_CANONNAME)


