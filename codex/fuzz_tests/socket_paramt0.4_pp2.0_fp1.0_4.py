import socket
socket.if_indextoname(3)

# socket.if_nameindex()
# 返回所有网络接口的索引和名称的列表。
# 每个接口的元素都是一个元组，包含接口的索引和名称。
socket.if_nameindex()

# socket.if_nametoindex(if_name)
# 返回给定网络接口的索引。
# 如果没有给定名称的接口，则引发异常socket.error。
socket.if_nametoindex('lo')

# socket.gethostbyaddr(ip_address)
# 返回IP地址的主机名
