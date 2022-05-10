import socket
socket.if_indextoname('3')

# 获取指定网卡的IP地址
socket.if_nameindex('en0')

# 获取本地主机名
socket.gethostname()

# 获取本地IP
socket.gethostbyname(socket.gethostname())

# 获取指定IP的主机名
socket.gethostbyaddr('127.0.0.1')

# 获取指定主机名的IP地址列表
socket.gethostbyname_ex('www.baidu.com')

# 获取主机名
socket.getfqdn('www.baidu.com')

# 获取指定IP的主机名
socket.getnameinfo(('127.0.0.1', 80), 0)

# 获取
