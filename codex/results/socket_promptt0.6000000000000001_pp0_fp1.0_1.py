import socket
# Test socket.if_indextoname()
try:
    print(socket.if_indextoname(1))
except OSError as e:
    print(e)
    print('SKIP')
    raise SystemExit

# Test socket.if_nameindex()
try:
    print(socket.if_nameindex())
except OSError as e:
    print(e)
    print('SKIP')
    raise SystemExit

# Test socket.if_nametoindex()
try:
    print(socket.if_nametoindex('lo'))
    print(socket.if_nametoindex('eth0'))
except OSError as e:
    print(e)
    print('SKIP')
    raise SystemExit

# Test socket.getifaddrs()
try:
    print(socket.getifaddrs())
except OSError as e:
    print(e)
    print('SKIP')
    raise SystemExit
