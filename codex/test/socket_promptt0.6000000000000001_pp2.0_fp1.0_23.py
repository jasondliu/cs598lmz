import socket
# Test socket.if_indextoname
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

n = s.if_nametoindex('lo')

if n != 1:
    raise RuntimeError('lo should have index 1')

if s.if_indextoname(n) != 'lo':
    raise RuntimeError('lo should have index 1')

if s.if_indextoname(99) is not None:
    raise RuntimeError('no index 99')

