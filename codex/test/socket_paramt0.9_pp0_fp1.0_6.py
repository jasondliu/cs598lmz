import socket
socket.if_indextoname(i)

# get extended stats from the network interface
import struct
def get_sock_extended(s):
    buf=s.getsockopt(socket.SOL_SOCKET, SO_EE_ORIGIN_TIMESTAMPING, 12)
    ts = struct.unpack('IIII', buf)
