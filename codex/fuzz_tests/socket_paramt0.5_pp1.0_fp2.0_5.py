import socket
socket.if_indextoname(3)

# 使用if_nameindex()函数可以获取接口的索引号和名字
socket.if_nameindex()

# 获取全部接口信息
socket.if_nameinfo(('127.0.0.1', 80))

# 获取接口的地址信息
socket.getaddrinfo('www.baidu.com', 'http')

# 获取本机的全部地址
socket.gethostbyname_ex(socket.gethostname())

# 获取本机的全部地址
socket.gethostbyname_ex('localhost')

# 获取本机的IP地址
socket.gethostbyname(socket.gethostname())

# 获取本机
