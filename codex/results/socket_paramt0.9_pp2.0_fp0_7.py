import socket
socket.if_indextoname(2)

host = socket.gethostname() 
print("host name",host)

ip = socket.gethostbyname(host)
print("ip address",ip)


import socket
ip = '127.0.0.1'
socket.gethostbyaddr(ip)

ip = '10.0.1.1'
socket.gethostbyaddr(ip)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("gmail.com",80))
print(s.getsockname()[0])
s.close()

import socket
import fcntl
import struct
def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', bytes(ifname,'utf-8')[:15])
   
