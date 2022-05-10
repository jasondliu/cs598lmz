import socket
# Test socket.if_indextoname()
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', 0))
sock.connect(('127.0.0.1', 80))
print(sock.getsockname()[1])
sock.close()

# Test socket.if_nametoindex()
print(socket.if_nametoindex('lo'))

# Test socket.getifaddrs()
print(socket.getifaddrs())

# Test socket.if_nameindex()
print(socket.if_nameindex())

# Test socket.if_freenameindex()
print(socket.if_freenameindex([(1, 'lo'), (2, 'eth0')]))

# Test socket.gethostbyname()
print(socket.gethostbyname('localhost'))

# Test socket.gethostbyname_ex()
print(socket.gethostbyname_ex('localhost'))

# Test socket.gethostbyaddr()
