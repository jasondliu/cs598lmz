import socket
socket.if_indextoname(1)

#if_nameindex()
#返回所有网络接口的索引和名称的元组列表
socket.if_nameindex()

#if_nametoindex(if_name)
#根据接口名称返回接口索引
socket.if_nametoindex('eth0')

#getservbyname(servicename[, protocolname])
#根据服务名称和协议名称返回服务协议号
socket.getservbyname('http','tcp')

#getservbyport(port[, protocolname])
#根据服务协议号和协议名称返回服务名称
socket.getserv
