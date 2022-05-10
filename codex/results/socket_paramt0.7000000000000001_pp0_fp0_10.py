import socket
socket.if_indextoname(3)

# socket.if_nameindex()
# 返回所有网络接口和索引的列表。
socket.if_nameindex()

# socket.if_nametoindex(ifname)
# 将网络接口的名字转换为索引。
socket.if_nametoindex('eth0')

# socket.gethostname()
# 返回当前主机名。
socket.gethostname()

# socket.gethostbyname(hostname)
# 根据主机名返回IP地址。
socket.gethostbyname('www.zhihu.com')

# socket.gethostbyname_ex(hostname)
# 根据主机名返回IP地址和额外信
