import socket
socket.if_indextoname(1)

# if_nameindex
socket.if_nameindex()

# if_nametoindex
socket.if_nametoindex('lo')

# gethostname
socket.gethostname()

# gethostbyname
socket.gethostbyname('localhost')
socket.gethostbyname('www.google.com')

# gethostbyname_ex
socket.gethostbyname_ex('localhost')
socket.gethostbyname_ex('www.google.com')

# gethostbyaddr
socket.gethostbyaddr('127.0.0.1')

# getaddrinfo
socket.getaddrinfo('localhost', 80)
socket.getaddrinfo('www.google.com', 80)

# getnameinfo
socket.getnameinfo(('127.0.0.1', 80), 0)
socket.getnameinfo(('www.google.com', 80), 0)

# getdefaulttimeout
socket.getdefaulttimeout()

# setdefaulttimeout
socket.setdefaulttimeout(10)

# getprotobyname
socket.
