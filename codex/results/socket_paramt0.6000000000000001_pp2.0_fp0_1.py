import socket
socket.if_indextoname(1)

# 查看网卡名称

import socket
socket.gethostbyname('www.python.org')

# 查看网址IP地址

import socket
socket.gethostbyname_ex('www.python.org')

# 查看网址IP地址，并提供IP地址列表

import socket
socket.gethostname()

# 查看计算机名称

import socket
socket.gethostbyaddr('127.0.0.1')

# 查看IP地址对应的主机名称

import socket
socket.getprotobyname('tcp')

# 查看协议名称对应的协议号

import socket
socket.getservbyname
