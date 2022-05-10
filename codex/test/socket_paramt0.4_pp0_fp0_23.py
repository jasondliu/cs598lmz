import socket
socket.if_indextoname(3)

# socket.if_nameindex()
# 返回所有网络接口的索引和名称的列表
socket.if_nameindex()

# socket.if_nametoindex(if_name)
# 将网络接口名称映射到索引
socket.if_nametoindex('lo')

# socket.gethostbyaddr(ip_address)
# 根据ip地址获取主机名和别名
socket.gethostbyaddr('127.0.0.1')

# socket.gethostbyname(hostname)
# 根据主机名获取ip地址
socket.gethostbyname('localhost')

# socket.gethostbyname_ex(hostname)
# 根据主
