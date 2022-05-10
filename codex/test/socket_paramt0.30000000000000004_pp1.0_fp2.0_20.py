import socket
socket.if_indextoname(1)

# if_nametoindex()
import socket
socket.if_nametoindex('eth0')

# if_nameindex()
import socket
socket.if_nameindex()

# if_freenameindex()
import socket
socket.if_freenameindex()

# gethostbyname()
import socket
socket.gethostbyname('www.python.org')

# gethostbyname_ex()
import socket
socket.gethostbyname_ex('www.python.org')

# gethostbyaddr()
import socket
socket.gethostbyaddr('216.58.209.206')

# getnameinfo()
import socket
socket.getnameinfo(('216.58.209.206', 80), 0)

# getaddrinfo()
import socket
socket.getaddrinfo('www.python.org', 'http')

# getdefaulttimeout()
import socket
socket.getdefaulttimeout()

# setdefaulttimeout()
import socket
socket.setdefaulttimeout(10)

# gethostname()
import socket
