import socket
socket.if_indextoname(3)

# socket.if_nameindex()
# 返回所有网络接口的索引和名称的列表
socket.if_nameindex()

# socket.if_nametoindex(if_name)
# 返回网络接口的索引
socket.if_nametoindex('eth0')

# socket.gethostbyaddr(ip_address)
# 返回一个元组，包含所有主机名，别名和IP地址
socket.gethostbyaddr('192.168.1.1')

# socket.gethostbyname(hostname)
# 返回主机名的IP地址
socket.gethostbyname('www.baidu.com')

# socket.gethostbyname_ex(hostname)

