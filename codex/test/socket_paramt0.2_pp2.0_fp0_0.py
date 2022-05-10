import socket
socket.if_indextoname(3)

# 列出所有的网络接口
socket.if_nameindex()

# 获取本机名
socket.gethostname()

# 获取本机的IP地址
socket.gethostbyname(socket.gethostname())

# 获取本机的IP地址列表
socket.gethostbyname_ex(socket.gethostname())

# 获取本机的MAC地址
socket.gethostbyname_ex(socket.gethostname())[2]

# 获取本机的MAC地址
socket.gethostbyname_ex(socket.gethostname())[2][0]

# 获取本机的MAC地址
socket.gethostbyname_ex(socket.gethostname())[2][1]

# 获取本
