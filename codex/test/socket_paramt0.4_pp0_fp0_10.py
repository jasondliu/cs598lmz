import socket
socket.if_indextoname(3)

# 获取接口的索引号
import socket
socket.if_nametoindex('en0')

# 获取本地接口信息
import socket
socket.getaddrinfo('localhost', 80, proto=socket.IPPROTO_TCP)

# 获取本地接口的IP地址
import socket
socket.gethostbyname('localhost')

# 获取本地接口的域名
import socket
socket.gethostname()

# 获取本地接口的信息
import socket
socket.gethostbyaddr('127.0.0.1')

# 获取本地接口的IP地址
import socket
socket.gethostbyname_ex('localhost')

# 获取本地接口的
