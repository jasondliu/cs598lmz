import socket
socket.if_indextoname(3)

#获取接口的索引
socket.if_nametoindex('en0')

#获取接口的状态
socket.if_nameindex()

#获取接口的信息
socket.if_nameinfo(('127.0.0.1', 0))

#获取接口的状态
socket.if_freenameindex()

#获取接口的信息
socket.if_getsockaddr(('127.0.0.1', 0))

#获取接口的信息
socket.if_gethostbyaddr('127.0.0.1')

#获取接口的信息
socket.if_gethostbyname('127.0.0.1')

#获取接口的
