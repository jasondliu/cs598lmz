import socket
socket.if_indextoname(1)

# 地址转换
socket.htons(80)
socket.ntohs(80)
socket.inet_aton('127.0.0.1')
socket.inet_ntoa(b'\x7f\x00\x00\x01')

# 获取本机名称
socket.gethostname()

# 获取本机地址
socket.gethostbyname('localhost')
socket.gethostbyname_ex('localhost')
socket.gethostbyaddr('127.0.0.1')

# 获取本机IP地址
socket.getaddrinfo('localhost', 80, 0, 0, socket.IPPROTO_TCP)
socket.getaddrinfo('localhost', 80, 0, 0, socket.IPPROTO_TCP, socket.AI_CANONNAME)
socket.getaddrinfo('localhost', 80, socket.AF_INET, socket.SOCK_STREAM, socket.IP
