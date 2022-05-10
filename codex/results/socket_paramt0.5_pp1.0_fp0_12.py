import socket
socket.if_indextoname(3)

# ipv4 address
socket.gethostbyname('www.google.com')
socket.gethostbyname_ex('www.google.com')

# ipv6 address
socket.getaddrinfo('www.google.com', 80, 0, 0, socket.IPPROTO_TCP)

# dns
socket.gethostbyaddr('216.58.194.174')
