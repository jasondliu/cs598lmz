import socket
socket.if_indextoname(3)

# socket.if_nameindex()
# 返回所有网络接口的索引和名字的列表
socket.if_nameindex()

# socket.if_nametoindex(if_name)
# 返回接口名字的索引
socket.if_nametoindex('lo')

# socket.gethostbyname(hostname)
# 返回主机名的IP地址
socket.gethostbyname('www.baidu.com')

# socket.gethostbyname_ex(hostname)
# 返回主机名的IP地址，别名和主机名
socket.gethostbyname_ex('www.baidu.com')

# socket.gethostname()
# 返回当前主机名
