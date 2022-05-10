import socket
socket.if_indextoname(3)

# 使用if_nameindex获取所有网络接口的名称和索引
socket.if_nameindex()

# 使用ioctl获取接口的状态
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
SIOCGIFADDR = 0x8915
ifreq = struct.pack('16sH14s', b'lo', socket.AF_INET, b'\x00'*14)
try:
    res = fcntl.ioctl(s.fileno(), SIOCGIFADDR, ifreq)
except:
    print('Error: ioctl')
else:
    ip = struct.unpack('16sH2x4s8x', res)[2]
    print(socket.inet_ntoa(ip))

# 使用ioctl获取接口的MAC地
