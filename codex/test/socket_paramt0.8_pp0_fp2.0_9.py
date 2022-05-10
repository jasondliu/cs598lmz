import socket
socket.if_indextoname(1)

s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
print(s.getsockname()[0])
s.close()

from netifaces import interfaces, ifaddresses, AF_INET
for interface in interfaces():
    for link in ifaddresses(interface)[AF_INET]:
        print(link['addr'])
