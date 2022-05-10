import socket
socket.if_indextoname(3)

#获取网络接口的索引
socket.if_nameindex()

#获取本地主机的名称
socket.gethostname()

#获取本地主机的详细信息
socket.gethostbyname_ex(socket.gethostname())

#获取本地主机的IP地址
socket.gethostbyname(socket.gethostname())

#获取远程主机的IP地址
socket.gethostbyname('www.baidu.com')

#获取远程主机的详细信息
socket.gethostbyname_ex('www.baidu.com')

#获取服务器的地址
socket.gets
