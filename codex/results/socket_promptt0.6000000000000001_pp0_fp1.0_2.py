import socket
# Test socket.if_indextoname()
if_indextoname(1)

# Test socket.if_nameindex()
if_nameindex()

# Test socket.if_nametoindex()
if_nametoindex('lo')

# Test socket.getaddrinfo()
getaddrinfo('localhost', 'http')

# Test socket.getnameinfo()
getnameinfo(('127.0.0.1', 80), 0)

# Test socket.gethostbyname()
gethostbyname('localhost')

# Test socket.gethostbyname_ex()
gethostbyname_ex('localhost')

# Test socket.gethostbyaddr()
gethostbyaddr('127.0.0.1')

# Test socket.gethostname()
gethostname()

# Test socket.getfqdn()
getfqdn('localhost')

# Test socket.socket()
socket(AF_INET, SOCK_STREAM)

# Test socket.socketpair()
socketpair(AF_INET, SOCK_STREAM)

# Test socket.fromfd()
from
