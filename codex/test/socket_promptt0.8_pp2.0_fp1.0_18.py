import socket
# Test socket.if_indextoname

if socket.has_ipv6:
    interface = socket.if_indextoname(1)
    addr = socket.gethostbyname(interface)
    if addr.startswith('fe80'):
        print('Test socket.if_indextoname passed.')

# Test socket.getaddrinfo exception

try:
    socket.getaddrinfo(1, 1)
except TypeError:
    print('Test socket.getaddrinfo passed.')

# Test socket.socket with proto

sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)


if sk.proto == socket.IPPROTO_TCP:
    print('Test socket.socket passed.')
else:
    print('Test socket.socket failed.')

sk.close()

# Test socket.socketpair

sk1, sk2 = socket.socketpair()

sk1.close()
sk2.close()
print('Test socket.socketpair passed.')

# Test UDP socket.sendto
