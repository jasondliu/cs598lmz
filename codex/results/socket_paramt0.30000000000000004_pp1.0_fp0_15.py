import socket
socket.if_indextoname(3)

# socket.if_nameindex()
# 返回所有网络接口的索引和名称的列表
socket.if_nameindex()

# socket.if_nametoindex(if_name)
# 返回接口的索引
socket.if_nametoindex('lo')

# socket.gethostbyname(hostname)
# 根据主机名返回IP地址
socket.gethostbyname('www.python.org')

# socket.gethostbyname_ex(hostname)
# 返回主机名的IP地址、别名列表和主机名
socket.gethostbyname_ex('www.python.org')

# socket.gethostname()
# 返回当前主机名
socket.get
