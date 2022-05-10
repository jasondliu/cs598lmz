import socket
socket.if_indextoname(1)

# 使用socket.gethostbyname_ex()获取主机名和IP地址
socket.gethostbyname_ex('www.python.org')

# 使用socket.gethostbyaddr()获取主机名和IP地址
socket.gethostbyaddr('127.0.0.1')

# 使用socket.getnameinfo()获取主机名和IP地址
socket.getnameinfo(('127.0.0.1', 80), 0)

# 使用socket.getfqdn()获取主机名和IP地址
socket.getfqdn('127.0.0.1')

# 使用socket.getaddrinfo()获取主机名和IP地址
socket.getaddrinfo('www.python.org', 'http
