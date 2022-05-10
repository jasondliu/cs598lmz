import socket
socket.if_indextoname(3)

import pcapy
pcapy.findalldevs()

# Python 2
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
s.bind(('', 9090))
s.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)

# Python 3
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('', 9090))
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 0)

# Python 2
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1
