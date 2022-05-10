import socket
socket.if_indextoname(3)

# 使用if_nameindex()获取所有网络接口
socket.if_nameindex()

# 使用if_nametoindex()获取指定网络接口的索引
socket.if_nametoindex('lo')

# 使用gethostbyname()获取主机名对应的IP地址
socket.gethostbyname('www.baidu.com')

# 使用gethostbyname_ex()获取主机名对应的IP地址，主机名和别名列表
socket.gethostbyname_ex('www.baidu.com')

# 使用gethostname()获取本机主机名
socket.gethostname()

# 使
