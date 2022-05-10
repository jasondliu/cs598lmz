import socket
socket.if_indextoname(3)

# 使用if_nameindex()函数获取网络接口的索引和名称
socket.if_nameindex()

# 使用if_nametoindex()函数获取网络接口的索引
socket.if_nametoindex('eth0')

# 使用gethostbyname()函数获取主机名对应的IP地址
socket.gethostbyname('www.baidu.com')

# 使用gethostbyname_ex()函数获取主机名对应的IP地址
socket.gethostbyname_ex('www.baidu.com')

# 使用gethostbyaddr()函数获取IP地址对应的主机
