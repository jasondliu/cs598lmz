import socket
socket.if_indextoname(3)

# 使用socket.if_nameindex()方法获取所有网络接口的名称和索引
socket.if_nameindex()

# 使用socket.if_nametoindex()方法获取指定网络接口的索引
socket.if_nametoindex('lo')

# 使用socket.gethostbyname()方法获取主机名对应的IP地址
socket.gethostbyname('www.baidu.com')

# 使用socket.gethostbyname_ex()方法获取主机名对应的IP地址和别名
socket.gethostbyname_ex('www.baidu.com')

# 使用socket.gethostbyaddr()方法
