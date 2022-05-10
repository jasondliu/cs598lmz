import socket
socket.if_indextoname('1')

# if_nametoindex()
import socket
socket.if_nametoindex('lo')

# gethostname()
import socket
socket.gethostname()

# gethostbyname()
import socket
socket.gethostbyname('www.google.com')

# gethostbyaddr()
import socket
socket.gethostbyaddr('216.58.207.206')

# getfqdn()
import socket
socket.getfqdn('216.58.207.206')

# getaddrinfo()
import socket
socket.getaddrinfo('www.google.com', 80)

# getnameinfo()
import socket
socket.getnameinfo(('216.58.207.206', 80), 0)

# getprotobyname()
import socket
socket.getprotobyname('tcp')

# getservbyname()
import socket
socket.getservbyname('http', 'tcp')

# getdefaulttimeout()
import socket
socket.getdefaulttimeout()

# setdefaulttimeout()
import socket
socket.
