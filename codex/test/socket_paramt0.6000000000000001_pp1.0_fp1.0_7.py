import socket
socket.if_indextoname(2)

# 使用gethostbyname_ex 获取主机的完全名称
socket.gethostbyname_ex('www.python.org')


# 使用gethostbyaddr 获取主机的IP地址
socket.gethostbyaddr('127.0.0.1')
