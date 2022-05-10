import socket
socket.if_indextoname(1)

# 利用socket.if_nameindex()获取网络接口信息
socket.if_nameindex()

# 利用socket.if_nametoindex()获取网络接口信息
socket.if_nametoindex('lo')

# 利用socket.getaddrinfo()获取网络接口信息
socket.getaddrinfo('www.baidu.com', 80)

# 利用socket.gethostbyname()获取网络接口信息
socket.gethostbyname('www.baidu.com')

# 利用socket.gethostbyname_ex()获取网络接口信息
socket.gethostbyname_ex('www.baidu.com')

