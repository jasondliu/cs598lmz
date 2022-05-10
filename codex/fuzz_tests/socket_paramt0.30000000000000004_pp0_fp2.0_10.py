import socket
socket.if_indextoname(1)

# 使用socket.gethostbyname_ex()函数获取主机名
socket.gethostbyname_ex('www.baidu.com')

# 使用socket.gethostbyname()函数获取主机名
socket.gethostbyname('www.baidu.com')

# 使用socket.gethostname()函数获取主机名
socket.gethostname()

# 使用socket.gethostbyaddr()函数获取主机名
socket.gethostbyaddr('127.0.0.1')

# 使用socket.getnameinfo()函数获取主机名
socket.getnameinfo(('127.0.0.1', 80), 0)

# 使用socket.getservbyname()函数获取主机名
socket
