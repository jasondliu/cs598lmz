import socket
socket.if_indextoname(32)

# 网络接口属性
import socket
socket.if_nametoindex('eth0')

# 获取本地IP
import socket
socket.gethostbyname(socket.gethostname())

# 获取本地IP
import socket
socket.gethostbyname_ex(socket.gethostname())

# 获取指定主机名的IP
import socket
socket.gethostbyname('www.baidu.com')

# 获取指定主机名的IP
import socket
socket.gethostbyname_ex('www.baidu.com')

# 获取指定主机名的IP
import socket
socket.getaddrinfo('www.baidu.com', 80)

# 获取指定主机名的IP 和 端口
import socket
socket
