import socket
socket.if_indextoname(0x1)

# 获取当前终端的所有网络接口
socket.if_nameindex()

# 获取本地地址，返回一个元组
socket.gethostbyname_ex('localhost')

# 获取主机名
socket.gethostname()

# 建立TCP客户端

s = socket.socket()
host = socket.gethostname()
port = 12345

s.connect((host, port))
