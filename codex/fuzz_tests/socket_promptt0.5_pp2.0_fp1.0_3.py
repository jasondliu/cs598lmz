import socket
# Test socket.if_indextoname()

socket.if_indextoname(1)

# Test socket.if_nameindex()

socket.if_nameindex()

# Test socket.if_nametoindex()

socket.if_nametoindex('lo')

# Test socket.getaddrinfo()

socket.getaddrinfo('localhost', 80)

# Test socket.getnameinfo()

socket.getnameinfo(('127.0.0.1', 80), 0)

# Test socket.getdefaulttimeout()

socket.getdefaulttimeout()

# Test socket.setdefaulttimeout()

socket.setdefaulttimeout(1.0)

# Test socket.socketpair()

socket.socketpair()

# Test socket.fromfd()

socket.fromfd(0, socket.AF_INET, socket.SOCK_STREAM)

# Test socket.socket()

socket.socket()

# Test socket.create_connection()

socket.create_connection(('localhost', 80))

# Test socket.gethostname()

socket.gethostname()
