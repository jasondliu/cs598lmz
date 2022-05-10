import socket
import struct
import sys

# (1) create a raw socket and bind it to the public interface
s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
s.bind((sys.argv[1], 0))

# (2) include IP headers
s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

# (3) receive all packages
s.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

# (4) receive a package
