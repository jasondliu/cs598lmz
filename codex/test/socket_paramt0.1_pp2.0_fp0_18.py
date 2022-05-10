import socket
socket.if_indextoname(3)

# socket.if_nameindex()
# 返回所有网络接口的索引和名称的列表
socket.if_nameindex()

# socket.if_nametoindex(if_name)
# 返回网络接口的索引
socket.if_nametoindex('lo')

# socket.gethostbyaddr(ip_address)
# 返回一个元组，其中包含主机名，别名列表和IP地址列表
socket.gethostbyaddr('127.0.0.1')

# socket.gethostbyname(hostname)
# 返回主机名的IP地址
socket.gethostbyname('localhost')

# socket.gethostbyname_ex(hostname)

