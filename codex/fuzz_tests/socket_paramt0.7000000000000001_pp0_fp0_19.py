import socket
socket.if_indextoname(1)

# Check for configured interfaces
from netifaces import interfaces, ifaddresses, AF_INET, AF_INET6

for interface in interfaces():
    try:
        print(interface, ifaddresses(interface)[AF_INET][0]['addr'])
    except KeyError:
        pass  # ignore ifaces that dont have IPv4
