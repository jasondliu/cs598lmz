import socket
socket.if_indextoname(3)

# if_nameindex()
# 返回所有网络接口的索引和名字的列表
socket.if_nameindex()

# if_nametoindex()
# 返回网络接口的索引
socket.if_nametoindex('eth0')

# gethostname()
# 返回当前主机的名字
socket.gethostname()

# gethostbyname()
# 返回主机名对应的IP地址
socket.gethostbyname('www.baidu.com')

# gethostbyname_ex()
# 返回主机名对应的IP地址和别名
socket.gethostbyname_ex('www.baidu.com')

# gethostbyaddr()
#
