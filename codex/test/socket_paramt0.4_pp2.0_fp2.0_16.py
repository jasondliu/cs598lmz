import socket
socket.if_indextoname(3)

# 使用socket模块的gethostname()函数返回本地主机名
print(socket.gethostname())

# 使用socket模块的gethostbyname()函数返回本地主机名对应的IP地址
print(socket.gethostbyname('localhost'))

# 使用socket模块的gethostbyname_ex()函数返回本地主机名对应的IP地址，可能有多个
print(socket.gethostbyname_ex('localhost'))

# 使用socket模块的gethostbyname_ex()函数返回本地主机名对应的IP地址，可能有多个
print
