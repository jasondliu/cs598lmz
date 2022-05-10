import socket
socket.if_indextoname(1)

# socket.if_nameindex()
# 返回所有网络接口的索引和名称的列表
socket.if_nameindex()

# socket.if_nametoindex(if_name)
# 返回网络接口的索引
socket.if_nametoindex('lo')

# socket.gethostbyaddr(ip_address)
# 把一个IP地址转换为一个包含主机名和别名的元组
socket.gethostbyaddr('127.0.0.1')

# socket.gethostbyname(hostname)
# 把一个主机名转换为一个IP地址
socket.gethostbyname('localhost')

# socket.gethostbyname_ex(
