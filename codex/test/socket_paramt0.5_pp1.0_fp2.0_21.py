import socket
socket.if_indextoname(2)

# 'en0'

socket.if_indextoname(3)

# 'en1'

socket.if_indextoname(4)

# 'lo0'

socket.if_indextoname(5)

# 'awdl0'

socket.if_indextoname(6)

# 'bridge0'

# You can also get the index of a network interface by name:
socket.if_nametoindex('lo0')

# 4

socket.if_nametoindex('awdl0')

# 5

# Here is a quick example that connects to a site and prints out the
# first 1024 bytes of the response.
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('www.python.org', 80))
s.sendall(b'GET /index.html HTTP/1.0\r\nHost: www.python.org\r\n\r\n')
data = s.recv(1024)

