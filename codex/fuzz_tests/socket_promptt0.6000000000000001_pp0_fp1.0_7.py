import socket
# Test socket.if_indextoname

def test(family):
    addr = socket.inet_pton(family, '127.0.0.1')
    if_index = socket.if_nametoindex('lo')
    if_name = socket.if_indextoname(if_index)
    sock = socket.socket(family, socket.SOCK_DGRAM)
    sock.bind((addr, 0), if_name)
    sock.close()

test(socket.AF_INET)
test(socket.AF_INET6)
