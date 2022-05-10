import socket
socket.if_indextoname(3)

# 查看网卡信息
import netifaces
netifaces.interfaces()
netifaces.ifaddresses('eth0')
netifaces.ifaddresses('eth0')[netifaces.AF_INET][0]['addr']

# 获取本机IP
import socket
socket.gethostbyname(socket.gethostname())

# 获取本机MAC
import uuid
uuid.UUID(int=uuid.getnode()).hex[-12:]

# 获取本机MAC
import uuid
mac = uuid.UUID(int=uuid.getnode()).hex[-12:]
mac = ":".join([mac[e:e+2] for e in range(0,11,2)])

# 获取本机MAC
import uuid
mac = uuid.UUID(int=uuid.getnode()).hex[-12:]
mac = ":".join
