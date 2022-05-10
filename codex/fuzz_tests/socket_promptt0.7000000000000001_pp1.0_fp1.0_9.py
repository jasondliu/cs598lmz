import socket
# Test socket.if_indextoname()
import socket
socket.if_indextoname(1)

# Test socket.gethostbyname_ex()
import socket
socket.gethostbyname_ex('localhost')

# Test socket.getfqdn()
import socket
socket.getfqdn('localhost')

# Test socket.getaddrinfo()
import socket
socket.getaddrinfo('localhost', 'http')

# Test socket.getnameinfo()
import socket
socket.getnameinfo(('127.0.0.1', 80), 0)

# Test socket.create_connection()
import socket
socket.create_connection(('localhost', 80))

# Test socket.getaddrinfo()
# Issue #7342: ipv6host can be a scopeid.
import socket
socket.getaddrinfo("::1%0", 80, socket.AF_INET6)[0][4][0]

# Test socket.inet_ntop()
import socket
socket.inet_ntop(socket.AF_INET, b'\x7f\x00\x00\x01')
