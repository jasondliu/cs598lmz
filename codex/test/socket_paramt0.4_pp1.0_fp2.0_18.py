import socket
socket.if_indextoname(3)

# get the name of an interface
socket.if_nameindex()

# get the address of an interface
socket.if_nametoindex('eth0')

# get the address of an interface
socket.gethostbyname('www.python.org')

# get the address of an interface
socket.gethostbyname_ex('www.python.org')

# get the address of an interface
socket.gethostbyaddr('127.0.0.1')

# get the address of an interface
socket.getfqdn('127.0.0.1')

# get the address of an interface
socket.gethostname()

# get the address of an interface
socket.gethostbyname_ex(socket.gethostname())

# get the address of an interface
socket.gethostbyname_ex(socket.getfqdn())

# get the address of an interface
socket.getaddrinfo('www.python.org', 'http')

# get the address of an interface
