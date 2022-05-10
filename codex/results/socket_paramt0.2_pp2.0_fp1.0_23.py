import socket
socket.if_indextoname(2)

# 获取本机IP地址
socket.gethostbyname(socket.gethostname())

# 获取本机MAC地址
def get_mac_address():
    mac=uuid.UUID(int = uuid.getnode()).hex[-12:]
    return ":".join([mac[e:e+2] for e in range(0,11,2)])

# 获取本机主机名
socket.gethostname()

# 获取本机所有网卡名称
socket.gethostbyname_ex(socket.gethostname())

# 获取本机所有网卡的IP地址
socket.gethostbyname_ex(socket.gethostname())[2]

# 获取本机所有网卡的MAC地址

