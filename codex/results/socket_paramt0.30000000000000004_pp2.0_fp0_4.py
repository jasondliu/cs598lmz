import socket
socket.if_indextoname(3)

# 使用if_nameindex()函数获取所有网络接口的名字和索引
socket.if_nameindex()

# 使用if_nametoindex()函数获取指定网络接口的索引
socket.if_nametoindex('eth0')

# 使用gethostname()函数获取主机名
socket.gethostname()

# 使用gethostbyname()函数获取主机的IP地址
socket.gethostbyname('www.baidu.com')

# 使用gethostbyname_ex()函数获取主机的IP地址、别名和地址类型
socket.gethostby
