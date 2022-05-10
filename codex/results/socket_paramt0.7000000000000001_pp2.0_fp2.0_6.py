import socket
socket.if_indextoname("1")

# 将字符串形式的ip地址转化为整数表达形式
socket.ntohl(struct.unpack("I",socket.inet_aton("127.0.0.1"))[0])

# 将整数形式的ip地址转化为字符串表达形式
socket.inet_ntoa(struct.pack("I",socket.htonl(2130706433)))

# 获取本机的IP地址
socket.gethostbyname(socket.gethostname())

#获取本机的MAC地址
socket.gethostbyname(socket.gethostname()).encode()

#############################################################

# 获取MAC地址
def get_mac_address():
    mac = uuid.UUID(
