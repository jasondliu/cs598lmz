import socket
socket.if_indextoname(14)

# 获取网卡名称
socket.gethostname()
# 获取主机名
socket.getfqdn(socket.gethostname())
# 获取网卡IP
socket.gethostbyname(socket.gethostname())
# 获取所有网卡IP
socket.gethostbyname_ex(socket.gethostname())
# 获取网卡第一个IP
socket.gethostbyname_ex(socket.gethostname())[2][0]
# 获取网卡第二个IP
socket.gethostbyname_ex(socket.gethostname())[2][1]
# 获取网卡所有IP
socket.gethostbyname_ex(socket.gethostname())[2]
