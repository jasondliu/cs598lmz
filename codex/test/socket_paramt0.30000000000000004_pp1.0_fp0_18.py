import socket
socket.if_indextoname(3)

# 可以使用socket.gethostbyname()函数来获取主机名对应的IP地址
socket.gethostbyname('www.python.org')

# 可以使用socket.gethostbyaddr()函数来获取IP地址对应的主机名
socket.gethostbyaddr('8.8.8.8')

# 可以使用socket.gethostname()函数来获取当前主机的主机名
socket.gethostname()

# 可以使用socket.getfqdn()函数来获取当前主机的完全限定域名
socket.getfqdn()

# 可以使用socket.getaddrinfo()函数
