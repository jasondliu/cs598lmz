import socket
socket.if_indextoname(3)

# socket.if_nameindex()
# 返回所有网络接口的索引和名称的列表
socket.if_nameindex()

# socket.if_nametoindex(interfaceName)
# 返回接口名称的索引
socket.if_nametoindex('en0')

# socket.gethostbyname(hostname)
# 返回主机名的 IP 地址
socket.gethostbyname('www.python.org')

# socket.gethostbyname_ex(hostname)
# 返回主机名的 IP 地址和别名列表
socket.gethostbyname_ex('www.python.org')

# socket.gethostname()
# 返回当前主机名
socket.gethostname()

