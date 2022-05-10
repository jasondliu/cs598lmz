import socket
# Test socket.if_indextoname() without a real interface.
sock = socket.socket(socket.AF_PACKET)
try:
    socket.if_indextoname(sock.fileno(), 0)
except OSError as ex:
    if ex.args[0] == errno.EINVAL:
        print('passed')
