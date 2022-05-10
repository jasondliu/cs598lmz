import socket
socket.if_indextoname(17)

# get IPv6 address of an interface
import socket
socket.if_nameindex()

# get fully qualified host name
import socket
socket.getfqdn()

# get the current machine host name
import socket
socket.gethostname()

# resolving host names to IPv4 addresses
import socket
socket.gethostbyname()

# get all configured IPv4 addresses
import socket
socket.gethostbyname_ex('webcode.me')

# resolve host name and port to socket addresses
import socket
socket.getaddrinfo('webcode.me', 8080)

# get all addresses of the host 
import socket
socket.getaddrinfo('webcode.me', 80, 0, 0, socket.IPPROTO_TCP, socket.AI_ALL)

# get the default socket timeout value
import socket
socket.getdefaulttimeout()

# get the current address family
import socket
socket.AF_INET

# get the current socket type
import socket
socket.SOCK_STREAM

# get the current protocol number
import socket
socket.IP
