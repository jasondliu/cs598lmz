import socket
socket.if_indextoname(3)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto(b'', ('8.8.8.8', 0))
s.getsockname()[0]

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(('8.8.8.8', 80))
s.getsockname()[0]

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(('127.0.0.1', 80))
s.getsockname()[0]

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
try:
    s.connect(('127.0.0.1', 80))
except socket.error:
    print("Fail")

socket.has_ipv6

socket.ip_address_list()

socket.getfqdn("8.8.8.8")

socket.gethostby
