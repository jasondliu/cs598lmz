import socket
socket.if_indextoname(3)

socket.if_nametoindex('en0')

socket.gethostbyname('www.python.org')

socket.gethostbyname_ex('www.python.org')

socket.gethostbyaddr('93.184.216.34')

socket.getprotobyname('tcp')

socket.getservbyname('http', 'tcp')

socket.getservbyport(80, 'tcp')

socket.getaddrinfo('www.python.org', 'http')

socket.getaddrinfo('www.python.org', 80, 0, 0, socket.IPPROTO_TCP)

socket.getaddrinfo('www.python.org', 80, 0, 0, socket.IPPROTO_TCP, socket.AI_CANONNAME)

socket.getnameinfo(('93.184.216.34', 80), socket.NI_NUMERICHOST)

socket.getnameinfo(('93.184.216.34', 80), 0)

socket.getnameinfo(('93.184.216.34
