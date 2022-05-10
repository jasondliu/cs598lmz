import socket
socket.if_indextoname(1)
socket.if_nametoindex('eth0')

# if_nameindex()
# if_freenameindex()

# gethostbyname()
# gethostbyname_ex()
# gethostbyaddr()
# getnameinfo()
# getaddrinfo()

# gethostname()
# getfqdn()

# getprotobyname()
# getservbyname()
# getservbyport()

# getdefaulttimeout()
# setdefaulttimeout()

# gethostbyname_ex()
socket.gethostbyname_ex('www.python.org')

# gethostbyaddr()
socket.gethostbyaddr('216.58.192.14')

# getaddrinfo()
socket.getaddrinfo('www.python.org', 'http')

# getnameinfo()
socket.getnameinfo(('216.58.192.14', 80), 0)

# gethostname()
socket.gethostname()

# getfqdn()
socket.getfqdn()

# getprotobyname
