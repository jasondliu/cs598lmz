import socket
socket.if_indextoname(3)

#if_nameindex()
#返回所有网络接口的索引和名称的列表
socket.if_nameindex()

#if_nametoindex(if_name)
#返回网络接口的索引
socket.if_nametoindex('lo')

#gethostbyname(hostname)
#返回主机名的IP地址
socket.gethostbyname('localhost')

#gethostbyname_ex(hostname)
#返回主机名的IP地址、别名列表和主机名
socket.gethostbyname_ex('localhost')

#gethostname()
#返回当前主机名
socket.gethostname()

#gethostbyaddr(ip_address)
#返回
