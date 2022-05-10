import socket
socket.if_indextoname(1)

#获取网卡的MAC地址
import fcntl
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
info = fcntl.ioctl(s.fileno(), 0x8927,  struct.pack('256s', b'eth0'))
mac = ''.join(['%02x:' % char for char in info[18:24]])[:-1]
print(mac)

#获取所有网卡的MAC地址
from uuid import getnode as get_mac
mac = get_mac()
mac = ':'.join(("%012X" % mac)[i:i+2] for i in range(0, 12, 2))
print(mac)

#获取主机名
import socket
socket.gethostname()

#获取IP地址
import socket
socket.gethostbyname(socket.gethostname())


