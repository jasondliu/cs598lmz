import socket
socket.if_indextoname(3)

# gethostbyname_ex
import socket
socket.gethostbyname_ex('www.python.org')

# gethostbyaddr
import socket
socket.gethostbyaddr('216.58.192.142')

# getnameinfo
import socket
socket.getnameinfo(('216.58.192.142', 80), 0)

# getfqdn
import socket
socket.getfqdn('216.58.192.142')

# getaddrinfo
import socket
socket.getaddrinfo('www.python.org', 'http')

# getdefaulttimeout
import socket
socket.getdefaulttimeout()

# setdefaulttimeout
import socket
socket.setdefaulttimeout(10)

# create_connection
import socket
socket.create_connection(('www.python.org', 80))

# SocketType
import socket
socket.SocketType

# socket
import socket
s = socket.socket()

# socketpair
import socket
socket.socketpair()

# fromfd
import socket
socket.fromfd(3, socket.AF
