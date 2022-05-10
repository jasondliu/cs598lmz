import socket
# Test socket.if_indextoname()
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ip = socket.inet_ntoa(fcntl.ioctl(sock.fileno(), 0x8915, struct.pack('256s', bytes('eth0', 'utf-8')))[20:24])
print(ip)
