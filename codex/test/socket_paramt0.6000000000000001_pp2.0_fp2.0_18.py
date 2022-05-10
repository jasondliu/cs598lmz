import socket
socket.if_indextoname(socket.if_nametoindex("lo"))

# IPv4
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((socket.gethostname(), 1234))

# IPv6
s = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
s.bind((socket.gethostname(), 1234))

# UDP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((socket.gethostname(), 1234))

# TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))

# UDP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((socket.gethostname(), 1234))
s.sendto(b"Hello", ("127.0.0.1", 1234))
s.recvfrom(1024)

# TCP
