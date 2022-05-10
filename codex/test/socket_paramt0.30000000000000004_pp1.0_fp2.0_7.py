import socket
socket.if_indextoname(3)

# socket.if_nameindex()
# 返回所有网络接口的索引和名称的列表。

# socket.if_nametoindex(if_name)
# 返回给定网络接口的索引。

# socket.gethostbyaddr(ip_address)
# 返回一个元组(hostname, aliaslist, ipaddrlist)，其中aliaslist和ipaddrlist分别是别名和IP地址列表。

# socket.gethostbyname(hostname)
# 返回主机名对应的IP地址。

# socket.gethostbyname_ex(hostname)
# 返回一个元组(hostname, aliaslist, ipaddrlist)
