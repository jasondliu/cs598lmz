import socket
socket.if_indextoname(3)

# 主机名称
socket.gethostname()

# 获取主机信息
socket.gethostbyname_ex('www.baidu.com')
socket.gethostbyname_ex('www.baidu.com')[2]
socket.gethostbyname_ex('www.baidu.com')[2][0]

# 获取端口信息
socket.getservbyname('http')

# 获取本地地址
socket.gethostbyname(socket.gethostname())

# 获取本地地址
socket.gethostbyname(socket.gethostname())
