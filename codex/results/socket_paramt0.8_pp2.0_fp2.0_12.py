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
print s.recv(1024)
s.close()

# 建立TCP服务器

import socket

s = socket.socket()
host = socket.gethostname()
post = 12346

s.bind((host, port))

s.listen(5)

while True:
    c, addr = s.accept()

    print 'Got connection
