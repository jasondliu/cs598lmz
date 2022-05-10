import socket
# Test socket.if_indextoname()
from socket import AF_INET, SOCK_DGRAM
from socket import if_indextoname

ifname = if_indextoname(1)

sk = socket.socket(AF_INET, SOCK_DGRAM)
sk.bind((ifname, 0))
