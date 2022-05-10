import socket
# Test socket.if_indextoname()
socket.if_indextoname(0)

# Test socket.gethostbyname_ex()
socket.gethostbyname_ex('localhost')

# Test socket.gethostbyname()
socket.gethostbyname('localhost')

# Test socket.gethostname()
socket.gethostname()

# Test socket.getaddrinfo()
socket.getaddrinfo('localhost', 80, socket.AF_INET, socket.SOCK_STREAM)

# Test socket.getfqdn()
socket.getfqdn('localhost')

# Test socket.getnameinfo()
socket.getnameinfo(('127.0.0.1', 80), 0)
# socket.getnameinfo(('localhost', 80), 0)

# Test socket.getservbyname()
socket.getservbyname('http')

# Test socket.getdefaulttimeout()
socket.getdefaulttimeout()

# Test socket.setdefaulttimeout()
socket.setdefaulttimeout(0.1)
socket.getdefaulttimeout()

# Test socket.getprotobyname
