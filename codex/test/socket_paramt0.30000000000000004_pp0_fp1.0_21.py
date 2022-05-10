import socket
socket.if_indextoname(3)

# 使用socket.gethostbyname()函数获取主机名对应的IP地址
socket.gethostbyname('www.baidu.com')

# 使用socket.gethostbyname_ex()函数获取主机名对应的IP地址
socket.gethostbyname_ex('www.baidu.com')

# 使用socket.gethostname()函数获取本机主机名
socket.gethostname()

# 使用socket.gethostbyaddr()函数获取IP地址对应的主机名
socket.gethostbyaddr('127.0.0.1')

# 使用socket.getfqdn()函数获取本机全名
